from flask import Flask, jsonify, Response, request
from flask_pymongo import PyMongo
from flask_restx import Api, Resource, fields
from bson.json_util import dumps


app = Flask(__name__)
app.config.from_prefixed_env()
app.config['MONGO_URI']

api = Api(app)
mongo = PyMongo(app)


@api.route('/movies')
class Movies(Resource):
    def get(self):
        data = dumps(mongo.db.movies.find())
        return Response(data, mimetype='aplication/json')
    def post(self):
        new_movie = request.get_json()
        mongo.db.movies.insert_one(new_movie)
        data = dumps(mongo.db.movies.find({'title': new_movie["title"]}))
        return Response(data, status=201, mimetype='aplication/json')

@api.route('/movies/<string:title>')
class OneMovie(Resource):
    def get(self, title):
        data = dumps(mongo.db.movies.find_one_or_404({"title": title}))
        return Response(data, mimetype='aplication/json')
            









# prediction_model = api.model('Data', {
#     'username': fields.String(required=True, description='Name of the data'),
#     'HomeTeam': fields.String(required=True, description='Value of the data'),
#     'AwayTeam': fields.String(required=True, description='Value of the data'),
#     'HomeTeamGoals': fields.Integer(required=True, description='Value of the data'),
#     'AwayTeamGoals': fields.Integer(required=True, description='Value of the data')
# })

@api.route('/matches')
class AllMatches(Resource):
    def get(self):
        data = dumps(mongo.db.matches.find())
        return Response(data, mimetype='aplication/json')

@api.route('/matches/<string:id>')
class OneMatch(Resource):
    def get(self, id):
        data = dumps(mongo.db.matches.find_one_or_404({'HomeTeam': id}))
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