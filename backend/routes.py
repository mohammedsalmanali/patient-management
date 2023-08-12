from flask import jsonify   # pylint: disable=import-error
from app import app  # Assuming 'app' is the Flask app instance

# Sample data for demonstration purposes
dashboard_data = {
    "activitySeries": [10, 20, 15, 30, 25],  # Replace with your actual data
    "metricsSeries": [70, 85, 90, 75, 80]    # Replace with your actual data
}

health_activities = [
    {"name": "Running", "date": "2023-08-01"},
    {"name": "Yoga", "date": "2023-08-02"},
    {"name": "Cycling", "date": "2023-08-03"},
    # ... Add more activities here
]

@app.route('/get_dashboard_data', methods=['GET'])
def get_dashboard_data():
    return jsonify(dashboard_data)

@app.route('/get_health_activities', methods=['GET'])
def get_health_activities():
    return jsonify(health_activities)
