# Configuration file that contains configurations for for Flask extensions in Config class
# Any additional configurations can be added to the class
# Any additional configuration SETS can be subclasses of the original Config class
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')