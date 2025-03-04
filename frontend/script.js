// This file contains JavaScript code for dynamic interactions on the frontend, such as form validation and updating prediction charts.

document.addEventListener('DOMContentLoaded', function() {
    const subscriptionForm = document.getElementById('subscription-form');
    const predictionChart = document.getElementById('prediction-chart');

    subscriptionForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const email = document.getElementById('email').value;

        if (validateEmail(email)) {
            subscribeUser(email);
        } else {
            alert('Please enter a valid email address.');
        }
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    function subscribeUser(email) {
        fetch('/api/subscribe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Subscription successful!');
                subscriptionForm.reset();
            } else {
                alert('Subscription failed. Please try again.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        });
    }

    function updatePredictionChart(data) {
        // Logic to update the prediction chart with new data
        // This function would typically use a charting library like Chart.js
    }

    // Fetch initial predictions and update the chart
    fetch('/api/predictions')
        .then(response => response.json())
        .then(data => {
            updatePredictionChart(data);
        })
        .catch((error) => {
            console.error('Error fetching predictions:', error);
        });
});