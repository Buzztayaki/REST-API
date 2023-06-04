from flask import Flask, jsonify, Response, request
from .databasequerys import mongo, matches, teamatches, classification, season_redCards, season_accuracy
from flask_restx import Api, Resource
from flask_cors import CORS


app = Flask(__name__)
app.config.from_prefixed_env()
app.config['MONGO_URI']
CORS(app)

api = Api(app)
mongo.init_app(app)

@api.route('/welcome')
class Home(Resource):
    def get(self):
        return {"message": "Welcome to my football API", "action": "Querie a defined endpoint"}

@api.route('/matches')
class AllMatches(Resource):
    def get(self):
            league = request.args.get("league")
            season = request.args.get("season")
            data = matches(league, season)
            return Response(data, mimetype='aplication/json')

@api.route('/matches/<string:team>')
class TeamMatches(Resource):
    def get(self, team):
        season = request.args.get("season")
        data = teamatches(team, season)
        return Response(data, mimetype='aplication/json')

@api.route('/classification/<string:league>')
class Clasification(Resource):
    def get(self, league):
            season = request.args.get("season")
            data = classification(league, season)
            return Response(data, mimetype='aplication/json')
    
@api.route('/leaguestats/redcards/<string:season>')
class RedCards(Resource):
    def get(self, season):
        data = season_redCards(season)
        return Response(data, mimetype='aplication/json')

@api.route('/leaguestats/accuracy/<string:season>')
class Accuracy(Resource):
    def get(self, season):
        data = season_accuracy(season)
        return Response(data, mimetype='aplication/json')