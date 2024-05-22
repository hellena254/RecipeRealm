#!/usr/bin/python3
"""define the routes for handling recipe-related requests"""

from flask import request, jsonify
from . import db
from .models import User, Recipe
from . import create_app


app = create_app()


@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """Get all recipes"""
    recipes = Recipe.query.all()
    return jsonify([{
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'author': recipe.author.username
    } for recipe in recipes])


@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    """Add a new recipe"""
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        description=data['description'],
        ingredients=data['ingredients'],
        instructions=data['instructions'],
        user_id=data['user_id']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe added successfully!'}), 201
