function handleFileSelect(input) {
    if (input.files && input.files.length > 0) {
        input.classList.add('green-input');
    } else {
        input.classList.remove('green-input');
    }
}


async function fetchColumnNames(fileInput, columnNameSelect, inputType) {
    console.log(`Fetching column names for ${inputType} users...`);

    const file = fileInput.files[0];
    if (!file) {
        alert(`Please select a file for ${inputType} users.`);
        return;
    }

    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/get_column_names', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const columnNames = await response.json();
            console.log(`Column names for ${inputType} users:`, columnNames);

            columnNameSelect.innerHTML = '';

            // Inside the fetchColumnNames function
            columnNames.forEach(encodedColumnName => {

                const columnName = decodeURIComponent(encodedColumnName).trim();

                const option = document.createElement('option');
                option.value = columnName;
                option.text = columnName;
                columnNameSelect.add(option);
            });


            console.log(`Column names for ${inputType} users:`, columnNames);

        } else {
            console.error(`Failed to fetch column names for ${inputType} users. Status: ${response.status}`);
            alert(`Failed to fetch column names for ${inputType} users. See console for details.`);
        }
    } catch (error) {
        console.error(`Error fetching column names for ${inputType} users:`, error);
    }
}

function toggleInput(fileInput, inputType) {
    const dropdown = document.getElementById(`${inputType}_column_name`);
    const input = document.getElementById(`${inputType}_column_name_input`);
    const checkbox = document.getElementById(`use_dropdown_${inputType}`);
    

    if (fileInput) {
        //input.style.display = 'none';  // Hide the input field
        //dropdown.style.display = 'inline'h

        handleFileSelect(fileInput) 

        fetchColumnNames(fileInput, dropdown, inputType);
    }// } else {
    //     input.style.display = 'inline';  // Show the input field
    //     dropdown.style.display = 'none';  // Hide the dropdown
    // }
}


document.addEventListener("DOMContentLoaded", function() {
    // Set initial visibility of dropdowns based on checkbox status
    toggleInput(document.getElementById('use_dropdown_all'), 'all');
      toggleInput(document.getElementById('use_dropdown_submitted'), 'submitted');
});

// Function to hide or show input based on checkbox status
function hideOrShowInput(inputType) {
    const checkbox = document.getElementById(`use_dropdown_${inputType}`);
    const input = document.getElementById(`${inputType}_column_name_input`);
    const dropdown = document.getElementById(`${inputType}_column_name`);

    if (checkbox.checked) {
        dropdown.style.display = 'inline';
        input.style.display = 'none';  // Hide the input field
        dropdown.style.transition = 'display 0.3s ease';
        fetchColumnNames(fileInput, dropdown, inputType);
        // Add logic here if needed for fetching column names
    } else {
        input.style.display = 'inline';  // Show the input field
        dropdown.style.display = 'none';  // Hide the dropdown
        dropdown.style.transition = 'display 0.3s ease';
    }
}
