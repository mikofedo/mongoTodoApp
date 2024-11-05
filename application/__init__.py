# __init__.py

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['SECRET_KEY'] = '8be30bb00390333bb542b482934ed545704f6dae'

app.config["MONGO_URI"]  ='mongodb+srv://q1biblio:DCqsoGKZuOZEwOYd@cluster0.lly3v.mongodb.net/qqdb?retryWrites=true&w=majority&appName=Cluster0'

mongo = PyMongo(app)
db = mongo.db
todos_collection = db.todos_flask

from application import routes

