from flask import Flask, request
import flask
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/players', methods=["GET"])
def players():
    print("users endpoint reached...")
    with open("players.json", "r") as f:
        data = json.load(f)
        '''data.append({
            "name": "Mike Trout",
            "teams": ["Angels"]
        })'''
        return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost", 1327)
    
#https://tms-dev-blog.com/python-backend-with-javascript-frontend-how-to/