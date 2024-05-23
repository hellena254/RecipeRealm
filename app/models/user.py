#!/usr/bin/python3
"""
User model defines the user details and relationships.
"""

from app import db


class User(db.Model):
    """
    User model to store user information.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    profile = db.relationship('UserProfile', uselist=False, back_populates='user')
    ratings = db.relationship('Rating', back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile': self.profile.to_dict() if self.profile else None,
            'ratings': [rating.to_dict() for rating in self.ratings]
        }
