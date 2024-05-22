#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Create and configure the flask app"""
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    with app.app_context():
        from app import routes
        from models.user import User
        from models.recipe import Recipe
        db.create_all()

    return app
