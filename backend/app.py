"""
Your module description here.
"""

from flask import Flask       # pylint: disable=import-error
from flask_sqlalchemy import SQLAlchemy    # pylint: disable=import-error
from flask_migrate import Migrate      # pylint: disable=import-error
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import User, HealthMetric  # Import models here

# Define API routes using Flask's @app.route
# For example: Create user, add health metric, get user data, etc.

if __name__ == '__main__':
    app.run(debug=True)
