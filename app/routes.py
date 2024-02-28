# This file is used to route each url request to a 'view' function module defined in the app package directory
from flask import render_template
from app import app

# These decorators attached above the function attach function to these URLS
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sydney'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland! (This is a post in the routes.py)'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Run those Js! (This is a post in the routes.py)'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)