import os
from flask import Flask
from flask_pymongo import PyMongo
from database import db


app = Flask(__name__)

db.connection()

@app.get('/')
def home ():
    return "Hello World"
