from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller.controller import controller

app = Flask(__name__)
app.register_blueprint(controller)

@app.route('/')
def index():
    return "Welcome to the Recipe API. Enjoy :)"

if __name__=="__main__":
    app.run(debug=True)

