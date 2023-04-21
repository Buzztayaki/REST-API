from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps



app = Flask(__name__)
app.config.from_prefixed_env()
app.config['MONGO_URI']
mongo = PyMongo(app)



@app.get('/')
def home ():
    vgames = mongo.db.games.find()
    