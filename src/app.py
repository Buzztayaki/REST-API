from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)

app.config.from_prefixed_env()
app.config['MONGO_URI']
mongo = PyMongo(app)







#mongo.db.games.find()

#app.add_url_rule()