# Configuration file that contains configurations for for Flask extensions in Config class
# Any additional configurations can be added to the class
# Any additional configuration SETS can be subclasses of the original Config class
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'