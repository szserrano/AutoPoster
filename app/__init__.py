# Initializing app as a flask instance. Importing routes at bottom to avoid circular imports
# Instructing Flask to read the config file and apply it using app.config.from_object() function 
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes