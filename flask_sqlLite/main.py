from flask import Flask, request, jsonify

app = Flask(__name__)

users = ["John", "Mark", "James", "Luke", "Matthew"]