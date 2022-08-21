from flask import Flask, request, jsonify
import request
application = Flask(__name__)
@application.route('/')
def hello_world():
    return 'Hello World'

@application.route('/user', methods=['GET','POST'])
def view_user():
    if request.method == 'GET':
        return "Hello, your name is" + request.form['name']