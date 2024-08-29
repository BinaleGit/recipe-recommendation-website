import unittest
import sys
import os

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models import Recipe

class RecipeModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.app.testing = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_recipe_creation(self):
        recipe = Recipe(
            title="Test Recipe",
            ingredients="test ingredients",
            instructions="test instructions",
            cooking_time=10,
            difficulty="easy",
            dietary_restrictions="none",
            rating=4.0
        )
        db.session.add(recipe)
        db.session.commit()
        self.assertEqual(Recipe.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
