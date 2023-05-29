from flask_pymongo import PyMongo
from bson.json_util import dumps


mongo = PyMongo()


def matches(League=None, Season=None):
    if League is None and Season is None:
        pipeline = [
            {"$addFields": { "Date": { "$dateFromString": { "dateString": "$Date", "format": "%d/%m/%Y" } } } }, 
            {"$sort": { "Date": -1 } }, 
            {"$limit": 10},
            { "$project": { "_id": 0, "Country": 1, "League": 1, "Season": 1, "Date": { "$dateToString": { "date": "$Date", "format": "%d/%m/%Y" } }, "HomeTeam": 1, "AwayTeam": 1, "HomeTeamGoals": 1, "AwayTeamGoals": 1, "Result": 1}}
        ]
        return dumps(mongo.db.matches.aggregate(pipeline))
    elif League is None:
        return dumps(mongo.db.matches.find({"Season": Season}))
    elif Season is None:
        return dumps(mongo.db.matches.find({"League": League}))
    else:
        return dumps(mongo.db.matches.find({"League": League, "Season": Season}))

def teamatches(Team, Season=None):
    if Season is None:
        pipeline = [
            {"$match": {"HomeTeam": Team}},
            {"$unionWith": {"coll": "matches", "pipeline": [{"$match": {"AwayTeam": Team}}]}},
            {"$addFields": { "Date": { "$dateFromString": { "dateString": "$Date", "format": "%d/%m/%Y"}}}},
            {"$sort": {"Date": -1}},
            { "$project": { "_id": 0, "Country": 1, "League": 1, "Season": 1, "Date": { "$dateToString": { "date": "$Date", "format": "%d/%m/%Y" } }, "HomeTeam": 1, "AwayTeam": 1, "HomeTeamGoals": 1, "AwayTeamGoals": 1, "Result": 1}}
        ]
        return dumps(mongo.db.matches.aggregate(pipeline))
    else:
        pipeline = [
            {"$match": {"HomeTeam": Team, "Season": Season}},
            {"$unionWith": {"coll": "matches", "pipeline": [{"$match": {"AwayTeam": Team, "Season": Season}}]}},
            {"$addFields": { "Date": { "$dateFromString": { "dateString": "$Date", "format": "%d/%m/%Y"}}}},
            {"$sort": {"Date": -1}}
        ]
        return dumps(mongo.db.matches.aggregate(pipeline))

def classification(League, Season):
    pipeline = [
        {"$match": {"League": League, "Season": Season}},
        {"$facet": {"homeTeamStats": [{"$group": {"_id": {"LeagueID": "$LeagueID", "Team": "$HomeTeam"},"MatchesPlayed": { "$sum": 1 }, "Wins": {"$sum": {"$cond": [{ "$eq": ["$Result", "H"] },1,0]}}, "Draws": {"$sum": {"$cond": [{ "$eq": ["$Result", "D"] },1,0]}}, "Losses": {"$sum": {"$cond": [{ "$eq": ["$Result", "A"] },1,0]}},"GoalsFor": { "$sum": "$HomeTeamGoals" }, "GoalsAgainst": { "$sum": "$AwayTeamGoals" }}},
            {"$project": {"Team": "$_id.Team","MatchesPlayed": 1,"Wins": 1,"Draws": 1,"Losses": 1,"GoalsFor": 1,"GoalsAgainst": 1,"GoalDifference": { "$subtract": ["$GoalsFor", "$GoalsAgainst"] }, "Points": {"$sum": [{ "$multiply": ["$Wins", 3] },"$Draws" ]}}}],"awayTeamStats": [
            {"$group": {"_id": {"LeagueID": "$LeagueID","Team": "$AwayTeam"},"MatchesPlayed": { "$sum": 1 },"Wins": {"$sum": {"$cond": [{ "$eq": ["$Result", "A"] },1,0]}},"Draws": {"$sum": {"$cond": [{ "$eq": ["$Result", "D"] },1,0]}},"Losses": {"$sum": {"$cond": [{ "$eq": ["$Result", "H"] },1,0]}},"GoalsFor": { "$sum": "$AwayTeamGoals" },"GoalsAgainst": { "$sum": "$HomeTeamGoals" }}},
            {"$project": {"Team": "$_id.Team","MatchesPlayed": 1,"Wins": 1,"Draws": 1,"Losses": 1,"GoalsFor": 1,"GoalsAgainst": 1,"GoalDifference": { "$subtract": ["$GoalsFor", "$GoalsAgainst"] },"Points": {"$sum": [{ "$multiply": ["$Wins", 3] },"$Draws"]}}}]}},
        {"$project": {"stats": { "$concatArrays": ["$homeTeamStats", "$awayTeamStats"] }}},
        {"$unwind": "$stats"},
        {"$replaceRoot": { "newRoot": "$stats" }},
        {"$group": {"_id": "$Team","MatchesPlayed": { "$sum": "$MatchesPlayed" }, "Wins": { "$sum": "$Wins" },"Draws": { "$sum": "$Draws" }, "Losses": { "$sum": "$Losses" }, "GoalsFor": { "$sum": "$GoalsFor" }, "GoalsAgainst": { "$sum": "$GoalsAgainst" }, "GoalDifference": { "$sum": "$GoalDifference" }, "Points": { "$sum": "$Points" }}},
        {"$sort": { "Points": -1, "GoalDifference": -1 }}
        ]
    return dumps(mongo.db.matches.aggregate(pipeline))

def season_redCards(Season):
    pipeline = [
        {"$match": {"Season": Season} },
        {"$group": {"_id": {"League": "$League", "Season": "$Season"},"RedCards": { "$sum": { "$add": ["$HomeTeamRedCards", "$AwayTeamRedCards"] } }}},
        {"$project": {"_id": 0,"League": "$_id.League","Season": "$_id.Season","RedCards": "$RedCards"}},
        {"$sort": {"League": 1}}
    ]
    return dumps(mongo.db.matches.aggregate(pipeline))

def season_accuracy(Season):
    pipeline = [
        {"$match": {"Season": Season} },
        {"$group": {"_id": "$League","totalShots": { "$sum": "$HomeTeamShots" }, "totalShotsTarget": { "$sum": "$HomeTeamShotsTarget" }}},
        {"$project": {"_id": 0, "League": "$_id", "Accuracy": { "$multiply": [ { "$divide": [ "$totalShotsTarget", "$totalShots" ] }, 100 ] }}},
        {"$project": {"League": 1, "Accuracy": { "$round": ["$Accuracy", 2] }}},
        {"$sort": {"League": 1}}
    ]
    return dumps(mongo.db.matches.aggregate(pipeline))