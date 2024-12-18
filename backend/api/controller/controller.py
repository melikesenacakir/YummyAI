import service.service as service
from flask import request
from flask import jsonify
from flask import Blueprint, request, jsonify


controller = Blueprint('controller', __name__)

@controller.route('/search', methods=['POST'])
def post_ingredients():
    data = request.get_json()
    ingredient = data.get('ingredients')
    if not ingredient:
        return jsonify({"error": "Ingredients not provided"}), 400
    return jsonify({"recipe":service.post_ingredients(ingredient)}),200