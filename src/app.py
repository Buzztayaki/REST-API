from flask import Flask, jsonify, Response
from flask_pymongo import PyMongo
from flask_restx import Api, Resource
from bson.json_util import dumps


app = Flask(__name__)
app.config.from_prefixed_env()
app.config['MONGO_URI']

api = Api(app)
mongo = PyMongo(app)


@api.route('/matches')
class AllMatches(Resource):
    def get(self):
        data = dumps(mongo.db.matches.find())
        return Response(data, mimetype='aplication/json')
    def post(self):
        pass

@api.route('/matches/<string:id>')
class OneMatch(Resource):
    def get(self, id):
        data = dumps(mongo.db.matches.find_one_or_404({'_id': "ObjectId({})".format(id)}))
        return Response(data, mimetype='aplication/json')
    def put(self, id):
        pass
    def delete(self, id):
        pass

@api.route('/predictions')
class Predictions(Resource):
    def get(self):
        pass
    def post(self):
        pass

#mongo.db.games.find()

#app.add_url_rule()