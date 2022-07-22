from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello World! Up and running. Send a POST request'
