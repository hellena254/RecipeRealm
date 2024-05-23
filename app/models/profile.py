#!/usr/bin/python3
"""
UserProfile model defines the profile details for a user.
"""

from app import db


class UserProfile(db.Model):
    """
    UserProfile model to store additional user information.
    """
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    bio = db.Column(db.String(500))
    profile_pic_url = db.Column(db.String(200))

    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f"<UserProfile for User {self.user_id}>"

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'bio': self.bio,
            'profile_pic_url': self.profile_pic_url
        }
