from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create a flask app and connect it to the SQLITE database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Create a model for the database
class User(db.Model):
    """
    User model for the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.name}', {self.age})"


# Create the database

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

# Path: flask_api/main.py
