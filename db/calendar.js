db.matches.aggregate(
    [
        {$match: {LeagueID: "SP1"},},
        {$project: {
            _id: 0,
            League: 1,
            HomeTeam: 1,
            AwayTeam: 1,
            HomeTeamGoals: 1,
            AwayTeamGoals: 1,
            Result: 1
            }
        },
        {
            $group: {
              _id: "$HomeTeam",
              MatchesPlayed: { $sum: 1 },
              Wins: {
                $sum: {
                  $cond: [
                    { $eq: ["$Result", "H"] },
                    1,
                    0
                  ]
                }
              },
              Draws: {
                $sum: {
                  $cond: [
                    { $eq: ["$Result", "D"] },
                    1,
                    0
                  ]
                }
              },
              Losses: {
                $sum: {
                  $cond: [
                    { $eq: ["$Result", "A"] },
                    1,
                    0
                  ]
                }
              },
              GoalsFor: { $sum: "$HomeTeamGoals" },
              GoalsAgainst: { $sum: "$AwayTeamGoals" }
            }
          },
          {
            $project: {
              Team: "$_id.Team",
              MatchesPlayed: 1,
              Wins: 1,
              Draws: 1,
              Losses: 1,
              GoalsFor: 1,
              GoalsAgainst: 1,
              GoalDifference: { $subtract: ["$GoalsFor", "$GoalsAgainst"] },
              Points: {
                $sum: [
                  { $multiply: ["$Wins", 3] },
                  "$Draws"
                ]
              }
            }
          },
          {
            $sort: { Points: -1, GoalDifference: -1 }
          }
    ] 
)

db.matches.aggregate(
  [
    {"$match": {Season: "2021-2022"} },
    {"$group": {
        "_id": {"League": "$League", "Season": "$Season"},
        "RedCards": { "$sum": { "$add": ["$HomeTeamRedCards", "$AwayTeamRedCards"] } }
      }
    },
    {"$project": {
        "_id": 0,
        "League": "$_id.League",
        "Season": "$_id.Season",
        "RedCards": "$RedCards"
      }
    },
    {"$sort": {RedCards: -1}}
  ]
)

db.matches.aggregate([
  {"$match": {"HomeTeam": "Sevilla", "Season": "2021-2022"}},
  {"$unionWith": {"coll": "matches", "pipeline": [{"$match": {"AwayTeam": "Betis", "Season": "2022-2023"}}]}},
  {"$addFields": { "Date": { "$dateFromString": { "dateString": "$Date", "format": "%d/%m/%Y"}}}},
  {"$sort": {"Date": -1}}
])