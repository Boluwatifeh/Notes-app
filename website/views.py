import json
from flask import Blueprint, jsonify

views = Blueprint('views', __name__)

@views.route("/")
def index():
    return jsonify({"message": "welcome to the home page"})