from flask import Flask
from flask_cors import CORS
from app.cache import cache
import sys

DEBUG = True

# instantiate the app
app = Flask(__name__)

cache.init_app(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

from app import database
from app import main
