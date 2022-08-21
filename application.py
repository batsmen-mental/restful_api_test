from flask import Flask, request

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Hello World'


@application.route('/user', methods=['GET', 'POST'])
def view_user():
    if request.method == 'GET':
        return "Hello, I dont know what your name is"
    if request.method == 'POST':
        name = request.form['name']
        return "Hello, your name is: " + name
