#!usr/bin/python3
"""Configuration for the application, including the database URI"""
import os


class Config:
    """Configuration class for the Flask application."""
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+mysqlconnector://reciperealm_user:recip3r3alm@localhost/reciperealm')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
