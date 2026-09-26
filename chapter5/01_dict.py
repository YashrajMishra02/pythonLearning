# create a empty dectionary
d = {}
# print(type(d))
marks = {
    "john":100,
    "harry":99,
    "deepak":98
}

marks['panda'] = 98.2 #adding key:value pair in dictonary 

marks['harry'] = 89.09 # Updation of value in dictonary

print(marks.get('chini','Not found'))  # Retrive the value of a specific key from a dictonary using get() method. If the key is not found, it returns 'Not found' with its 2nd argument.

marks.update({'harry':55,'deepak':77}) # Updating values of existing keys or adding new key-value pairs to the dictionary using update() method.

print(marks)

print(marks,type(marks))

print(marks["harry"]) # printing the value of a specific key in dictonary using key name.

print(marks.items()) # printing all key-value pairs in the dictionary

print(marks.keys())

marks.update({"friend":99.7}) # Adding a new key-value pair to the dictionary

print(marks)

print(marks.get("deepak")) # Retrieving the value of a specific key from the dictionary using get() method.

            # string        integers            List
student = {'name':'John', 'age': 25, 'courses':['Maths','CompSci']}

print(student['age'])

print(type(student['courses']))