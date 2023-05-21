from flask import Flask, jsonify, Response, request
from .databasequerys import mongo, matches, teamatches, classification, season_redCards
from flask_restx import Api, Resource
from src.databasequerys import matches


app = Flask(__name__)
app.config.from_prefixed_env()
app.config['MONGO_URI']

api = Api(app)
mongo.init_app(app)


@api.route('/matches')
class AllMatches(Resource):
    def get(self):
        if len(request.args) == 0 or len(request.args) > 2:
            return Response({"Query Params needed!"}, status=400, mimetype='application/json')
        else:
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
        data = classification(league)
        return Response(data, mimetype='aplication/json')
    
@api.route('/leaguestats/redcards/<string:season>')
class RedCards(Resource):
    def get(self, season):
        data = season_redCards(season)
        return Response(data, mimetype='aplication/json')