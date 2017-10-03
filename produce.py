from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    print(request.headers)
    return jsonify({'fooz': 'bar'})
