from flask import Flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return "Flask server is running"

# Others file
from controller import *
