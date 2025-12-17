#!/usr/bin/env python3
# server/app.py
from flask import Flask

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Route for dynamic user profiles
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# This block allows you to run the app using 'python app.py'
if __name__ == '__main__':
    app.run(port=5555, debug=True)