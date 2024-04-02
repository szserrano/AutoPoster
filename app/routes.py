# This file is used to route each url request to a 'view' function module defined in the app package directory
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

# These decorators attached above the function attach function to these URLS
@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', posts=posts)

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)