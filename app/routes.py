#!/usr/bin/python3
"""
Define the routes for handling recipe-related requests.
"""

from flask import Flask, request, jsonify
from app import db, create_app
from app.models.recipe import Recipe
from app.models.rating import Rating

app = create_app()


@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """
    GET endpoint to retrieve all recipes.
    Returns:
        JSON: List of all recipes in the database.
    """
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes]), 200


@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    """
    POST endpoint to add a new recipe.
    Returns:
        JSON: The newly created recipe.
    """
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
    return jsonify(new_recipe.to_dict()), 201


@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """
    PUT endpoint to update an existing recipe.
    Args:
        recipe_id (int): ID of the recipe to be updated.
    Returns:
        JSON: The updated recipe.
    """
    recipe = Recipe.query.get_or_404(recipe_id)

    data = request.get_json()
    
    # Update recipe data
    if 'title' in data:
        recipe.title = data['title']
    if 'description' in data:
        recipe.description = data['description']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'instructions' in data:
        recipe.instructions = data['instructions']

    db.session.commit()
    return jsonify(recipe.to_dict()), 200


@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """
    DELETE endpoint to delete an existing recipe.
    Args:
        recipe_id (int): ID of the recipe to be deleted.
    Returns:
        JSON: Message indicating the deletion status.
    """
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted successfully."}), 200


@app.route('/api/recipes/<int:recipe_id>/rate', methods=['POST'])
def rate_recipe(recipe_id):
    """
    POST endpoint to rate a recipe.
    Args:
        recipe_id (int): ID of the recipe to be rated.
    Returns:
        JSON: The newly created rating.
    """
    data = request.get_json()
    new_rating = Rating(
        user_id=data['user_id'],
        recipe_id=recipe_id,
        rating=data['rating'],
        comment=data.get('comment')
    )
    db.session.add(new_rating)
    db.session.commit()
    return jsonify(new_rating.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
