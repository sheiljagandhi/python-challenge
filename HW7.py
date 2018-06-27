
# coding: utf-8

# In[1]:


import json
import tweepy 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import time

# Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[3]:


target_user1 = "@foxnews" #,"@msnbc","@cnn","@bbc","@nytimes"

# Counter
counter = 1

# Variables for holding sentiments
sentiments1 = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user1)

    # Loop through all tweets 
    for tweet in public_tweets:

        # Print Tweets
        # print("Tweet %s: %s" % (counter, tweet["text"]))
        
        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        name = "Fox News"
        
        # Add sentiments for each tweet into an array
        sentiments1.append({"Media Source": name,
                           "Date": tweet["created_at"], 
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets Ago": counter})
 
        # Add to counter 
        counter = counter + 1

 #       # Print Analysis
 #       print(f"Compound Score: {compound}")
 #       print(f"Positive Score: {pos}")
 #       print(f"Neutral Score: {neu}")
 #       print(f"Negative Score: {neg}")

# Convert sentiments to DataFrame
sentiments1_pd = pd.DataFrame.from_dict(sentiments1)
sentiments1_pd.head()


# In[4]:


# Target Accounts
target_user2 = "@msnbc" #,"@cnn","@bbc","@nytimes"

# Counter
counter = 1

# Variables for holding sentiments
sentiments2 = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user2)

    # Loop through all tweets 
    for tweet in public_tweets:

        # Print Tweets
        # print("Tweet %s: %s" % (counter, tweet["text"]))
        
        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        name = "MSNBC"
        
        # Add sentiments for each tweet into an array
        sentiments2.append({"Media Source": name,
                           "Date": tweet["created_at"], 
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets Ago": counter})
 
        # Add to counter 
        counter = counter + 1
 
# Convert sentiments to DataFrame
sentiments2_pd = pd.DataFrame.from_dict(sentiments2)
sentiments2_pd.head()


# In[5]:


# Target Accounts
target_user3 = "@cnn" #,"@bbc","@nytimes"

# Counter
counter = 1

# Variables for holding sentiments
sentiments3 = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user3)

    # Loop through all tweets 
    for tweet in public_tweets:

        # Print Tweets
        # print("Tweet %s: %s" % (counter, tweet["text"]))
        
        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        name = "CNN"
        
        # Add sentiments for each tweet into an array
        sentiments3.append({"Media Source": name,
                           "Date": tweet["created_at"], 
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets Ago": counter})
 
        # Add to counter 
        counter = counter + 1
 
# Convert sentiments to DataFrame
sentiments3_pd = pd.DataFrame.from_dict(sentiments3)
sentiments3_pd.head()


# In[6]:


# Target Accounts
target_user4 = "@bbc"

# Counter
counter = 1

# Variables for holding sentiments
sentiments4 = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user4)

    # Loop through all tweets 
    for tweet in public_tweets:

        # Print Tweets
        # print("Tweet %s: %s" % (counter, tweet["text"]))
        
        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        name = "BBC"
        
        # Add sentiments for each tweet into an array
        sentiments4.append({"Media Source": name,
                           "Date": tweet["created_at"], 
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets Ago": counter})# Target Accounts
 
        # Add to counter 
        counter = counter + 1
 
# Convert sentiments to DataFrame
sentiments4_pd = pd.DataFrame.from_dict(sentiments4)
sentiments4_pd.head()


# In[7]:


# Target Accounts
target_user5 = "@nytimes"

# Counter
counter = 1

# Variables for holding sentiments
sentiments5 = []

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(5):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user5)

    # Loop through all tweets 
    for tweet in public_tweets:

        # Print Tweets
        # print("Tweet %s: %s" % (counter, tweet["text"]))
        
        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        name = "NYTimes"
        
        # Add sentiments for each tweet into an array
        sentiments5.append({"Media Source": name,
                           "Date": tweet["created_at"], 
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets Ago": counter})
 
        # Add to counter 
        counter = counter + 1
 
# Convert sentiments to DataFrame
sentiments5_pd = pd.DataFrame.from_dict(sentiments5)
sentiments5_pd.head()


# In[8]:


sentiments12_pd = pd.merge(sentiments1_pd, sentiments2_pd, how="outer", on=None)

sentiments123_pd = pd.merge(sentiments12_pd, sentiments3_pd, how="outer", on=None)

sentiments1234_pd = pd.merge(sentiments123_pd, sentiments4_pd, how="outer", on=None)

combined_sentiments_pd = pd.merge(sentiments1234_pd, sentiments5_pd, how="outer", on=None)

combined_sentiments_pd.head()


# In[9]:


target_users = "Fox News", "MSNBC", "CNN","BBC", "NYTimes"

# Create plot
plt.plot(np.arange(len(combined_sentiments_pd["Compound"])),
         combined_sentiments_pd["Compound"], marker="o", linewidth=0,
         alpha=0.8)

# # Incorporate the other graph properties
plt.title("Sentiment Analysis for Media Sources (%s) for %s" % (time.strftime("%x"),target_users))
plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")
plt.legend ("Media Sources")
plt.show()


# In[10]:


# Set x axis and tick locations
x_axis = np.arange(len(combined_sentiments_pd))
tick_locations = [value+0.4 for value in x_axis]

# Create a list indicating where to write x labels and set figure size to adjust for space
plt.figure(figsize=(20,3))
plt.bar(x_axis, combined_sentiments_pd["Compound"], color='r', alpha=0.5, align="edge")
plt.xticks(tick_locations, combined_sentiments_pd["Media Source"], rotation="vertical")

# Set x and y limits
plt.xlim(-0.25, len(x_axis))
plt.ylim(0, max(combined_sentiments_pd["Compound"])+1)

# # Incorporate the other graph properties
plt.title("Overall Media Alignment Based on Twitter (%s) for %s" % (time.strftime("%x"),target_users))
plt.ylabel("Tweet Polarity")
plt.xlabel("Media Source")
plt.legend ("Media Sources")
plt.show()


# In[11]:


# Export the new CSV
combined_sentiments_pd.to_csv("output/sentiments_df.csv", index=False)

