#!/usr/bin/python3

from flask import Flask
from flask_migrate import Migrate
from app import create_app, db

# Create the Flask application instance
app = create_app()

# Initialize database migration system
migrate = Migrate(app, db)
