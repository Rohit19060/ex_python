from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Rohit Jain", "age": 25},
]


@app.route("/")
def hello_world():
    return jsonify({"api": "Flask API"})


@app.route("/users")
def get_users():
    return jsonify(users)


@app.route("/get-user/<user_id>")
def get_user(user_id):
    for user in users:
        if user["id"] == int(user_id):
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404


@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    # if request.method == "POST":
    user_data = request.get_json()
    return jsonify(user_data), 201


# "get-user/123?extra=helloworld"

# GET
# POST
# PUT
# DELETE

if __name__ == "__main__":
    app.run(debug=True, port=8001)
