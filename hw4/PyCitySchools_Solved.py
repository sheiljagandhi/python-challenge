
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# In[1]:


import pandas as pd
import numpy as np
import os

schools_file = os.path.join('Resources','/Users/sheiljagandhi/Downloads/UCBSAN201805DATA1-master/02-Homework/04-Numpy-Pandas/Instructions/PyCitySchools/raw_data/schools_complete.csv')
students_file = os.path.join('Resources', '/Users/sheiljagandhi/Downloads/UCBSAN201805DATA1-master/02-Homework/04-Numpy-Pandas/Instructions/PyCitySchools/raw_data/students_complete.csv')

schools_df = pd.read_csv(schools_file)
students_df = pd.read_csv(students_file)


schools_df.rename(columns = {'name': 'school'}, inplace = True)
merged_df = students_df.merge(schools_df, how = 'left', on = 'school')


# ## District Summary

# In[2]:


unique_school_names = schools_df['school'].unique()
school_count = len(unique_school_names)
dist_student_count = schools_df['size'].sum()
total_student_rec = students_df['name'].count()

#Total Budget
total_budget = schools_df['budget'].sum()

num_passing_reading = students_df.loc[students_df['reading_score'] >= 70]['reading_score'].count()
perc_pass_reading = num_passing_reading/total_student_rec

num_passing_math = students_df.loc[students_df['math_score'] >= 70]['math_score'].count()
perc_pass_math = num_passing_math/total_student_rec

#Average Math Score 
avg_math_score = students_df['math_score'].mean()

#Average Reading Score
avg_reading_score = students_df['reading_score'].mean()

#Passing Rate
overall_pass = students_df[(students_df['math_score'] >= 70) & (students_df['reading_score'] >= 70)]['name'].count()/total_student_rec

#District Summary
district_summary = pd.DataFrame({
    
    "Total Schools": [school_count],
    "Total Students": [dist_student_count],
    "Total Budget": [total_budget],
    "Average Reading Score": [avg_reading_score],
    "Average Math Score": [avg_math_score],
    "% Passing Reading":[perc_pass_reading],
    "% Passing Math": [perc_pass_math],
    "Overall Passing Rate": [overall_pass]

})

#store as different df to change order
dist_sum = district_summary[["Total Schools", 
                             "Total Students", 
                             "Total Budget", 
                             "Average Reading Score", 
                             "Average Math Score", 
                             '% Passing Reading', 
                             '% Passing Math', 
                             'Overall Passing Rate']]

#format cells
dist_sum.style.format({"Total Budget": "${:,.2f}", 
                       "Average Reading Score": "{:.1f}", 
                       "Average Math Score": "{:.1f}", 
                       "% Passing Math": "{:.1%}", 
                       "% Passing Reading": "{:.1%}", 
                       "Overall Passing Rate": "{:.1%}"})



# ## School Summary

# In[3]:


#group by school
by_school = merged_df.set_index('school').groupby(['school'])

#school type
sch_types = schools_df.set_index('school')['type']

# total students 
stu_per_sch = by_school['Student ID'].count()

# school budget
sch_budget = schools_df.set_index('school')['budget']

#per student budget
stu_budget = schools_df.set_index('school')['budget']/schools_df.set_index('school')['size']

#avg scores by school
avg_math = by_school['math_score'].mean()
avg_read = by_school['reading_score'].mean()

# % passing scores
pass_math = merged_df[merged_df['math_score'] >= 70].groupby('school')['Student ID'].count()/stu_per_sch 
pass_read = merged_df[merged_df['reading_score'] >= 70].groupby('school')['Student ID'].count()/stu_per_sch 
overall = merged_df[(merged_df['reading_score'] >= 70) & (merged_df['math_score'] >= 70)].groupby('school')['Student ID'].count()/stu_per_sch 

sch_summary = pd.DataFrame({
    "School Type": sch_types,
    "Total Students": stu_per_sch,
    "Per Student Budget": stu_budget,
    "Total School Budget": sch_budget,
    "Average Math Score": avg_math,
    "Average Reading Score": avg_read,
    '% Passing Math': pass_math,
    '% Passing Reading': pass_read,
    "Overall Passing Rate": overall
})




#School Summary
sch_summary = sch_summary[['School Type', 
                          'Total Students', 
                          'Total School Budget', 
                          'Per Student Budget', 
                          'Average Math Score', 
                          'Average Reading Score',
                          '% Passing Math',
                          '% Passing Reading',
                          'Overall Passing Rate']]

#fSummary Format 
sch_summary.style.format({'Total Students': '{:,}', 
                          "Total School Budget": "${:,}", 
                          "Per Student Budget": "${:.0f}",
                          'Average Math Score': "{:.1f}", 
                          'Average Reading Score': "{:.1f}", 
                          "% Passing Math": "{:.1%}", 
                          "% Passing Reading": "{:.1%}", 
                          "Overall Passing Rate": "{:.1%}"})


# ## Top Performing Schools (By Passing Rate)

# In[4]:


# sort by passing rate (top 5) 
top_5 = sch_summary.sort_values("Overall Passing Rate", ascending = False)
top_5.head().style.format({'Total Students': '{:,}',
                           "Total School Budget": "${:,}", 
                           "Per Student Budget": "${:.0f}", 
                           "% Passing Math": "{:.1%}", 
                           "% Passing Reading": "{:.1%}", 
                           "Overall Passing Rate": "{:.1%}"})


# ## Bottom Performing Schools (By Passing Rate)

# In[5]:


#bottom 5 schools worse to best
bottom_5 = top_5.tail()
bottom_5 = bottom_5.sort_values('Overall Passing Rate')
bottom_5.style.format({'Total Students': '{:,}', 
                       "Total School Budget": "${:,}", 
                       "Per Student Budget": "${:.0f}", 
                       "% Passing Math": "{:.1%}", 
                       "% Passing Reading": "{:.1%}", 
                       "Overall Passing Rate": "{:.1%}"})


# ## Math Scores by Grade

# In[6]:


#grade level average math scores for ea. school 
ninth_math = students_df.loc[students_df['grade'] == '9th'].groupby('school')["math_score"].mean()
tenth_math = students_df.loc[students_df['grade'] == '10th'].groupby('school')["math_score"].mean()
eleventh_math = students_df.loc[students_df['grade'] == '11th'].groupby('school')["math_score"].mean()
twelfth_math = students_df.loc[students_df['grade'] == '12th'].groupby('school')["math_score"].mean()

math_scores = pd.DataFrame({
        "9th": ninth_math,
        "10th": tenth_math,
        "11th": eleventh_math,
        "12th": twelfth_math
})
math_scores = math_scores[['9th', '10th', '11th', '12th']]
math_scores.index.name = "School"

#show and format
math_scores.style.format({'9th': '{:.1f}', 
                          "10th": '{:.1f}', 
                          "11th": "{:.1f}", 
                          "12th": "{:.1f}"})


# ## Reading Score by Grade 

# In[7]:


#create grade level avg reading scores for ea. school
ninth_reading = students_df.loc[students_df['grade'] == '9th'].groupby('school')["reading_score"].mean()
tenth_reading = students_df.loc[students_df['grade'] == '10th'].groupby('school')["reading_score"].mean()
eleventh_reading = students_df.loc[students_df['grade'] == '11th'].groupby('school')["reading_score"].mean()
twelfth_reading = students_df.loc[students_df['grade'] == '12th'].groupby('school')["reading_score"].mean()

#merge the reading score averages by school and grade together
reading_scores = pd.DataFrame({
        "9th": ninth_reading,
        "10th": tenth_reading,
        "11th": eleventh_reading,
        "12th": twelfth_reading
})
reading_scores = reading_scores[['9th', '10th', '11th', '12th']]
reading_scores.index.name = "School"

#format
reading_scores.style.format({'9th': '{:.1f}', 
                             "10th": '{:.1f}', 
                             "11th": "{:.1f}", 
                             "12th": "{:.1f}"})


# ## Scores by School Spending

# In[8]:


# create spending bins
bins = [0, 584.999, 614.999, 644.999, 999999]
group_name = ['< $585', "$585 - 614", "$615 - 644", "> $644"]
merged_df['spending_bins'] = pd.cut(merged_df['budget']/merged_df['size'], bins, labels = group_name)

#group by spending
by_spending = merged_df.groupby('spending_bins')

#calcs
avg_math = by_spending['math_score'].mean()
avg_read = by_spending['reading_score'].mean()
pass_math = merged_df[merged_df['math_score'] >= 70].groupby('spending_bins')['Student ID'].count()/by_spending['Student ID'].count()
pass_read = merged_df[merged_df['reading_score'] >= 70].groupby('spending_bins')['Student ID'].count()/by_spending['Student ID'].count()
overall = merged_df[(merged_df['reading_score'] >= 70) & (merged_df['math_score'] >= 70)].groupby('spending_bins')['Student ID'].count()/by_spending['Student ID'].count()

            
# df build            
scores_by_spend = pd.DataFrame({
    "Average Math Score": avg_math,
    "Average Reading Score": avg_read,
    '% Passing Math': pass_math,
    '% Passing Reading': pass_read,
    "Overall Passing Rate": overall
            
})
            
#reorder colms
scores_by_spend = scores_by_spend[[
    "Average Math Score",
    "Average Reading Score",
    '% Passing Math',
    '% Passing Reading',
    "Overall Passing Rate"
]]

scores_by_spend.index.name = "Per Student Budget"
scores_by_spend = scores_by_spend.reindex(group_name)

#formating
scores_by_spend.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})


# ## Scores by School Size

# In[9]:


# create size bins
bins = [0, 999, 1999, 99999999999]
group_name = ["Small (<1000)", "Medium (1000-2000)" , "Large (>2000)"]
merged_df['size_bins'] = pd.cut(merged_df['size'], bins, labels = group_name)

#group by spending
by_size = merged_df.groupby('size_bins')

#calculations 
avg_math = by_size['math_score'].mean()
avg_read = by_size['math_score'].mean()
pass_math = merged_df[merged_df['math_score'] >= 70].groupby('size_bins')['Student ID'].count()/by_size['Student ID'].count()
pass_read = merged_df[merged_df['reading_score'] >= 70].groupby('size_bins')['Student ID'].count()/by_size['Student ID'].count()
overall = merged_df[(merged_df['reading_score'] >= 70) & (merged_df['math_score'] >= 70)].groupby('size_bins')['Student ID'].count()/by_size['Student ID'].count()

            
# df build            
scores_by_size = pd.DataFrame({
    "Average Math Score": avg_math,
    "Average Reading Score": avg_read,
    '% Passing Math': pass_math,
    '% Passing Reading': pass_read,
    "Overall Passing Rate": overall
            
})
            
#reorder columns
scores_by_size = scores_by_size[[
    "Average Math Score",
    "Average Reading Score",
    '% Passing Math',
    '% Passing Reading',
    "Overall Passing Rate"
]]

scores_by_size.index.name = "Total Students"
scores_by_size = scores_by_size.reindex(group_name)

#formating
scores_by_size.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})


# ## Scores by School Type

# In[11]:


# group by type of school
by_type = merged_df.groupby("type")

#calculations 
avg_math = by_type['math_score'].mean()
avg_read = by_type['math_score'].mean()
pass_math = merged_df[merged_df['math_score'] >= 70].groupby('type')['Student ID'].count()/by_type['Student ID'].count()
pass_read = merged_df[merged_df['reading_score'] >= 70].groupby('type')['Student ID'].count()/by_type['Student ID'].count()
overall = merged_df[(merged_df['reading_score'] >= 70) & (merged_df['math_score'] >= 70)].groupby('type')['Student ID'].count()/by_type['Student ID'].count()

# df build            
scores_by_type = pd.DataFrame({
    "Average Math Score": avg_math,
    "Average Reading Score": avg_read,
    '% Passing Math': pass_math,
    '% Passing Reading': pass_read,
    "Overall Passing Rate": overall})
    
#reorder columns
scores_by_type = scores_by_type[[
    "Average Math Score",
    "Average Reading Score",
    '% Passing Math',
    '% Passing Reading',
    "Overall Passing Rate"
]]
scores_by_type.index.name = "Type of School"


#formating
scores_by_type.style.format({'Average Math Score': '{:.1f}', 
                              'Average Reading Score': '{:.1f}', 
                              '% Passing Math': '{:.1%}', 
                              '% Passing Reading':'{:.1%}', 
                              'Overall Passing Rate': '{:.1%}'})

