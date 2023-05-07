from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_restplus import Api, Resource
from bson.json_util import dumps


app = Flask(__name__)
api = Api(app)

app.config.from_prefixed_env()
app.config['MONGO_URI']
mongo = PyMongo(app)




@api.route('/season')
class Season(Resource):
    def get(self):
        return 'Hello'




#mongo.db.games.find()

#app.add_url_rule()