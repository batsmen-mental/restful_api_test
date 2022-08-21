from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
    return 'Hello World'

@application.route('/user', methods=['GET','POST'])
def view_user():
    return "Hello, your name is" + request.form['name']