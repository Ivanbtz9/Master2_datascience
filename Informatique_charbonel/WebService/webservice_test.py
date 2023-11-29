#! /bin/env python3

from flask import Flask
import json


app = Flask(__name__)

d = { "un": 1, "deux": 2}

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/show', methods=['GET'])
def show():
    return json.dumps(d)

# http://127.0.0.1:5000/hello/toto
@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return f"Hello {name} !"

if __name__ == '__main__':
    app.run(debug=True)

