#!/usr/bin/python3
"""
Recipe model defines the recipe details and relationships.
"""

from app import db


class Recipe(db.Model):
    """
    Recipe model to store recipe information.
    """
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    ratings = db.relationship('Rating', back_populates='recipe', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Recipe {self.title}>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'instructions': self.instructions,
            'user_id': self.user_id,
            'ratings': [rating.to_dict() for rating in self.ratings]
        }
