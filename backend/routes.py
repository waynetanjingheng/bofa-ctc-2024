from flask import request, jsonify
from flask.blueprints import Blueprint
# import pandas as pd

api = Blueprint("api", __name__)

# Define all API endpoints for the backend here.


@api.route("/")
def index():
    response = jsonify({"message": "BOFA Code to Connect 2024"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    http_status_code = 200
    return response, http_status_code


@api.route("/health_check")
def health_check():
    return jsonify({"message": "Application Running..."}), 200
