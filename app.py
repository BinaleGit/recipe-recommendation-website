import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Recipe  # Import db from models.py

app = Flask(__name__)
CORS(app)

# Configure the database URI, pointing to an SQLite database in the root folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Route for the home page
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Recipe Recommendation API!"})

# Route to fetch all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_data = {
            "title": recipe.title,
            "ingredients": recipe.ingredients,
            "instructions": recipe.instructions,
            "cooking_time": recipe.cooking_time,
            "difficulty": recipe.difficulty,
            "dietary_restrictions": recipe.dietary_restrictions,
            "rating": recipe.rating
        }
        recipe_list.append(recipe_data)
    return jsonify(recipe_list)

# Main block to run the app and create the database
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
        
    # Run the Flask app
    app.run(debug=True)
