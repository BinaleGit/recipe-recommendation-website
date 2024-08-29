from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    dietary_restrictions = db.Column(db.String(200))
    rating = db.Column(db.Float)

    def __repr__(self):
        return f'<Recipe {self.title}>'
