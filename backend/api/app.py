from flask import Flask
from controller.controller import controller
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(controller)
CORS(app)

@app.route('/')
def index():
    return "Welcome to the Recipe API. Enjoy :)"

if __name__=="__main__":
    app.run(debug=True)

