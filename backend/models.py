"""
This module contains the main Flask application for the healthcare project.
It defines routes, controllers, and models for managing patient records.
"""

from flask_sqlalchemy import SQLAlchemy   # pylint: disable=import-error

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Add more fields like email, password, etc.

class HealthMetric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    metric_type = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
