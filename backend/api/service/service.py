import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from scripts.predict import predict


def post_ingredients(ingredients):
    recipes = predict(ingredients)
    return recipes