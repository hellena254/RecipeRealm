#!/usr/bin/python3
""" serve as the entry point to run the Flask application"""
from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
