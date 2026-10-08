# Dumping python object into json string

''' JavaScript Object Notation '''

import json # Its part of standard library

people_string = '''
{
    "people":
    [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com","john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

#  *** loads : methods convert json string into python object
data = json.loads(people_string) 

for person in data['people']:
    del person['phone']

# *** dumps : method convert python data(dictonary) into json string ***

new_string = json.dumps(data) # Without Formating
print(new_string)

new_string = json.dumps(data,indent=2) # With Formating
print(new_string)

new_string = json.dumps(data,indent=2,sort_keys=True) # sorting keys in json string
print(new_string)