# main driver script that initializes main application. When first running, run commands:
# $ source venv/Scripts/activate
# $ export FLASK_APP=autoposter.py
# $ flask run
#
# The decorator registers the function as a shell context function for when you need to run the python interpreter to test things out.
# * It utilizes a dictionary to map the objects imported to strings to be used to reference said objects in the shell
#
# To run this shell, you need the .flaskenv to have the FLASK_APP=autoposter.py in order to avoid NameErrors. When ready to run, input:
#   $ flask shell 
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}