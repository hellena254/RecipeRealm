#!/usr/bin/python3
"""Defining the user database model"""
from . import db

class User(db.Model):
    """Model for the user."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Column(db.String(200), nullable=False)
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __repr__(self):
        """String representation of an object"""
        return f"<User {self.username}>"
