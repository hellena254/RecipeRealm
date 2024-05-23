#!/usr/bin/python3
"""
Rating model defines the rating details for a recipe.
"""

from app import db


class Rating(db.Model):
    """
    Rating model to store ratings for recipes.
    """
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    recipe = db.relationship('Recipe', back_populates='ratings')
    user = db.relationship('User', back_populates='ratings')

    def __repr__(self):
        return f"<Rating {self.rating} for Recipe {self.recipe_id} by User {self.user_id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'recipe_id': self.recipe_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'timestamp': self.timestamp
        }
