# JSON - JavaScript Object Notation
import json

matches = [
    {
        'Team A': 'Portugal', 
        'Team B': 'Spain',
        'Score A': 1,
        'Score B': 1,
        'Date': '2024-04-15',
    },
    {
        'Team A': 'Germany', 
        'Team B': 'France',
        'Score A': 1,
        'Score B': 3,
        'Date': '2024-04-21',
    },
]
with open('matches.json', 'w') as file:
    json.dump(matches, file, indent=4)
