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

print(data) # Creates a dictonary

print(type(data)) # found using type method

print(data.get('people')) # value of key people is in the list 

print(type(data.get('people'))) # value of key people is in the list 

print(data.get('people')[0]) # Getting dic > list> index
print(data.get('people')[1]) # Getting dic > list> index

for person in data['people']:
    print(person['name'])

print(type(person))  # Here the person variable is a dictonary 
