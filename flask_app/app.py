from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    people = ["joaquin", "kevin", "jose"]

    return json.dumps(people)

@app.route("/<name>/")
def hello_world(name):
    data = json.dumps({"name": name})

    return data


@app.route("/<category>/book")
def hello_world(name, team):
    data = json.dumps({"name": name})

    return data