# This file is used to route each url request to a 'view' function module defined in the app package directory
from flask import render_template
from app import app

# These decorators attached above the function attach function to these URLS
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sydney'}
    return render_template('index.html', title='Home', user=user)