# This file is used to route each url request to a 'view' function module defined in the app package directory
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

# /login URL
#   * Initialize form to be instance from LoginForm() defined in apps.form.py module we created
#   * Passing newly instantiated form object to final return with the name 'form' gives template the object to work with during render
#   * form.validate_on_submit(): does form processing work. If the browser sends the GET request to receive web page w the form, 
#       this returns False (The Sign In form should send a POST request). When it sends false, we would see the Sign In form page again.
#   * flash function allows for receiving form data. Seeing how methods for the /login route are 'GET' and 'POST', the app must be able to receive form data.
#       The message in the flash() function is outputted when we are redirected to the url after the flash function. The .format() within the flash function
#       formats the arguments within the message respectively at the {}'s. You'd be able to see this message in the app/templates/base.html
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)