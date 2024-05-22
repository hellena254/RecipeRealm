#!/usr/bin/python3
"""define the routes for handling recipe-related requests"""

from flask import request, jsonify
from app import db
from app.models.user import User
from app.models.recipe import Recipe
from app import create_app


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


@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """Update an existing recipe"""
    recipe = Recipe.query.get_or_404(recipe_id)

    # extract updated data from request body
    data = request.json

    # update recipe data
    if 'title' in data:
        recipe.title = data['title']
    if 'description' in data:
        recipe.description = data['description']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'instructions' in data:
        recipe.instructions = data['instructions']

    # commit changes to the database
    db.session.commit()

    return jsonify({'message': 'Recipe updated successfully'})


@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """Delete recipe"""
    recipe = Recipe.query.get_or_404(recipe_id)

    # delete the recipe from the database
    db.session.delete(recipe)
    db.session.commit()

    return jsonify({'message': 'Recipe deleted successfully'})
