#!/usr/bin/python3
"""Defining the recipe database model"""
from app import db


class Recipe(db.Model):
    """Model for the recipe."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """String representation of an object"""
        return f"<Recipe {self.title}>"
