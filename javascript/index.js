// Get references to the tbody element, input field and button
var $tbody = document.querySelector('tbody');
var $stateInput = document.querySelector('#state');
var $searchBtn = document.querySelector('#search');

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener('click', handleSearchButtonClick);

// Set filteredAddresses to addressData initially
// addressData comes from the addressData.js file
var filteredAddresses = addressData;

// Fill the empty table with data from addressData
function renderTable() {
    $tbody.innerHTML = '';
    for (var i = 0; i < filteredAddresses.length; i++) {
      // Get get the current address object and its field
      var address = filteredAddresses[i];
      var fields = Object.keys(address);
      // Create a new row in the tbody, set the index to be i + startingIndex
      var $row = $tbody.insertRow(i);
      for (var j = 0; j < fields.length; j++) {
        // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = address[field];
      }
    }
  }

  function handleSearchButtonClick() {
    var filterState = $stateInput.value.trim().toLowerCase();
    filteredAddresses = addressData.filter(function(address) {
      var addressState = address.state.toLowerCase();
      return addressState === filterState;
    });

    renderTable();
    };

    function handleResetButtonClick() {
      filteredAddresses = addressData;
      $cityInput.value = '';
      $stateInput.value = '';
      renderTable();
    };
  
  // Render the table for the first time on page load
  renderTable();
