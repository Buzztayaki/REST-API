from flask_pymongo import PyMongo
from bson.json_util import dumps


mongo = PyMongo()


def matches(League=None, Season=None):
    if League is None and Season is None:
        return {"error": "Bad Request", "message": "No valid arguments"}
    elif League is None:
        return dumps(mongo.db.matches.find({"Season": Season}))
    elif Season is None:
        return dumps(mongo.db.matches.find({"League": League}))
    else:
        return dumps(mongo.db.matches.find({"Season": Season, "League": League}))

def teamatches(Team):
    pipeline = [
        {"$match": {"HomeTeam": Team}},
        {"$unionWith": {"coll": "matches", "pipeline": [{"$match": {"AwayTeam": Team}}]}}
    ]
    return dumps(mongo.db.matches.aggregate(pipeline))

def classification(League):
    pipeline = [
        {"$match": {"League": League}},
        {"$project": {"_id": 0, "League": 1, "HomeTeam": 1, "AwayTeam": 1, "HomeTeamGoals": 1, "AwayTeamGoals": 1, "Result": 1}},
        {"$group": {"_id": "$HomeTeam", "MatchesPlayed": { "$sum": 1 }, "Wins": { "$sum": { "$cond": [ { "$eq": ["$Result", "H"] }, 1, 0]}}, "Draws": { "$sum": { "$cond": [ { "$eq": ["$Result", "D"] }, 1, 0 ]}}, "Losses": { "$sum": { "$cond": [ { "$eq": ["$Result", "A"] }, 1, 0 ] } }, "GoalsFor": { "$sum": "$HomeTeamGoals" }, "GoalsAgainst": { "$sum": "$AwayTeamGoals" } } },
        {"$project": {"Team": "$_id.Team", "MatchesPlayed": 1, "Wins": 1, "Draws": 1, "Losses": 1, "GoalsFor": 1, "GoalsAgainst": 1, "GoalDifference": { "$subtract": ["$GoalsFor", "$GoalsAgainst"] }, "Points": { "$sum": [ { "$multiply": ["$Wins", 3] }, "$Draws" ] }}},
        {"$sort": { "Points": -1, "GoalDifference": -1 }}
    ]
    return dumps(mongo.db.matches.aggregate(pipeline))