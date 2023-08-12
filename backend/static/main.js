// Fetch and display dashboard data and health-related activities using AJAX

// Initialize charts using ApexCharts library
const activityChart = new ApexCharts(document.querySelector('#activity-chart'), {
    // Configuration for activity chart
});

const metricsChart = new ApexCharts(document.querySelector('#metrics-chart'), {
    // Configuration for metrics chart
});

// Fetch data and update charts
fetch('/get_dashboard_data')
    .then(response => response.json())
    .then(data => {
        // Update activity chart data
        activityChart.updateSeries(data.activitySeries);

        // Update metrics chart data
        metricsChart.updateSeries(data.metricsSeries);
    });

// Fetch data and update health activity list
fetch('/get_health_activities')
    .then(response => response.json())
    .then(data => {
        const activityList = document.getElementById('health-activities');
        activityList.innerHTML = '';

        data.forEach(activity => {
            const listItem = document.createElement('div');
            listItem.textContent = `Activity: ${activity.name}, Date: ${activity.date}`;
            activityList.appendChild(listItem);
        });
    });
