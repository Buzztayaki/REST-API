db.matches.aggregate(
    [
        {$match: { LeagueID: "SP1" } },
        {$group: { 
            _id: {
                local: "$HomeTeam",
                visitante: "$AwayTeam"
            },
            partidos_jugados: { $sum: 1 }    
            }
        }
    ] 
)

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