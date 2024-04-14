   

function clearTable() {
    // Show a confirmation dialog
    if (confirm("Your details has been cleared please reoald the page.")) {
        // If user confirms, send an AJAX request to the backend to clear the table
        fetch('/clear_table/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Add CSRF token
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // If the request is successful, clear the table on the frontend
                var tableBody = document.getElementById('surveyTableBody');
                tableBody.innerHTML = ''; // Clear the table body
            } else {
                console.error('Failed to clear table:', response.statusText);
            }
        })
        .catch(error => {
            console.error('Error clearing table:', error);
        });
    }
}



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



