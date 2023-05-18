db.calendar.insertMany([
    {
        Country: 'Spain',
        League: 'Primera Division',
        Date: new Date('2023-06-04'),
        HomeTeam: 'Betis',
        AwayTeam: 'Valencia',
    }
])

db.movies.insertMany(
    {
        _id: 1,
        title: 'El Padrino',
        releaseYear: 1972,
        director: 'Francis Ford Coppola',
        cast: ['Marlon Brando', 'Al Pacino', 'James Caan'],
        score: 92,
        platform: ['Netflix', 'Amazon Prime', 'HBO']
    }
)