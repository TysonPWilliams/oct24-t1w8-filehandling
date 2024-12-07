import json
with open('matches.json', 'r') as file:
    matches = json.load(file)
    print(type(matches))
    print(type(matches[0]))
    print(matches[0]['Date'])