# Initializing app as a flask instance. Importing routes at bottom to avoid circular imports
# Instructing Flask to read the config file and apply it using app.config.from_object() function 
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models