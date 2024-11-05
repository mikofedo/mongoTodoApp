# __init__.py

import os
from flask import Flask
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
uri = os.getenv('uri')
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the desired database and collection
db = client['qqdb']  # Replace <database> with your actual database name
todos_collection = db.todos_flask  # Make sure 'todos_flask' exists in the database

from application import routes