import json
from pstats import SortKey
from flask import Flask, request, jsonify
import re

# Create an instance of the Flask app
app = Flask(__name__)


# Define a route and its corresponding function
@app.route("/")
def hello_world():
    """
    Returns a greeting message.
    """
    return "Hello, World!"


users = [
    {"name": "John", "age": 20, "marks": 90},
    {"name": "Mary", "age": 21, "marks": 80},
    {"name": "Bob", "age": 19, "marks": 70},
]

students = [
    {"name": "John", "age": 20, "marks": 90},
    {"name": "Mary", "age": 21, "marks": 80},
    {"name": "Bob", "age": 19, "marks": 70},
]


# @app.route("/sortUser")
# def get_user():


@app.route("/users", methods=["GET", "POST"])
@app.route("/users/<index>", methods=["PUT", "DELETE", "GET"])
def create_user(index=None):
    """
    Create a user in the list of users.

    Args:
        index (int, optional): Index of the user to be created. Defaults to None.

    Returns:
        str: Message indicating the action performed.
    """
    if request.method == "POST":
        data = request.get_json()
        x = data["user"]
        users.append(x)
        return f"{x} added to the list!"
    elif request.method == "PUT":
        data = request.get_json()
        if index is None:
            updated = 0
        else:
            updated = int(index)
        x = data["user"]
        users[updated] = x
        return f"{x} updated in the list!"
    elif request.method == "DELETE":
        if index is None:
            updated = 0
        else:
            updated = int(index)
        x = users[updated]
        users.pop(updated)
        return f"{x} deleted from the list!"
    else:
        value = request.args["key"]
        if value is None:
            return jsonify(students)
        if value.lower() == "name":
            students.sort(key=lambda x: x["name"])
            return jsonify(students)
        elif value.lower() == "age":
            students.sort(key=lambda x: x["age"])
            return jsonify(students)
        elif value.lower() == "marks":
            students.sort(key=lambda x: x["marks"])
            return jsonify(students)
        else:
            return jsonify(students)


# Create a route to access query parameters
@app.route("/query")
def query():
    """
    Returns the query parameters.
    """
    # Get the query parameters from the URL
    name = request.args.get("name")
    location = request.args.get("location")
    return f"Hello {name}! You are from {location}."


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
