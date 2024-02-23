# Initializing app as a flask instance. Importing routes at bottom to avoid circular imports
from flask import Flask

app = Flask(__name__)

from app import routes