# Loading json file into python object

import json

with open('states.json') as f:
    # load method load json file into python object
    data = json.load(f)

for state in data['states']:
    # print(state)
    
    print(state['name'],state['abbreviation'])

print(type(state))