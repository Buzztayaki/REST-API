from flask import Flask, jsonify
import db
from flask_pymongo import PyMongo
from flask_restx import Api, Resource
from bson.json_util import dumps


app = Flask(__name__)
app.config.from_prefixed_env()
app.config['MONGO_URI']

api = Api(app)
mongo = PyMongo(app)




@api.route('/inicio')
class Season(Resource):
    def get(self):
        # data = mongo.db.football.find({'Country': 'Spain'})
        # print(data)
        return {"hola": "hola"}

#mongo.db.games.find()

#app.add_url_rule()