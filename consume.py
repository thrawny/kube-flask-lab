from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    r = requests.get('http://produce:5000', headers={'X-Something': 'foo'})
    return jsonify({'produce_response': r.json()})
