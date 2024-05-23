#!/usr/bin/python3
"""file initializes the models package and imports the individual model files"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


from app.models.user import User
from app.models.recipe import Recipe
from app.models.profile import UserProfile
from app.models.rating import Rating
