# __init__.py

# from flask import Flask
# from flask_pymongo import PyMongo

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://q1biblio:DCqsoGKZuOZEwOYd@cluster0.lly3v.mongodb.net/qqdb?retryWrites=true&w=majority&appName=Cluster0"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))


# app = Flask(__name__)

# app.config['SECRET_KEY'] = '8be30bb00390333bb542b482934ed545704f6dae'

# app.config["MONGO_URI"]  ='mongodb+srv://q1biblio:DCqsoGKZuOZEwOYd@cluster0.lly3v.mongodb.net/qqdb?retryWrites=true&w=majority&appName=Cluster0'

# mongo = PyMongo(app)
# db = mongo.db
# todos_collection = db.todos_flask

# from application import routes



from flask import Flask
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.config['SECRET_KEY'] = '8be30bb00390333bb542b482934ed545704f6dae'
uri = "mongodb+srv://q1biblio:DCqsoGKZuOZEwOYd@cluster0.lly3v.mongodb.net/qqdb?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the desired database and collection
db = client['qqdb']  # Replace <database> with your actual database name
todos_collection = db.todos_flask  # Make sure 'todos_flask' exists in the database

from application import routes