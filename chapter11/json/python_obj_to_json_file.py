# Converting python object into json file
import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_codes']

with open('new_states.json','w') as f:
# *** dump method convert data into json file ***
    json.dump(data, f,indent=2)

print(state.values())