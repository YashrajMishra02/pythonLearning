
# create a empty dectionary

d = {}

print(type(d))

marks = {
    "john":100,
    "harry":99,
    "deepak":98
}

print(marks)

marks['panda'] = 98.2 #adding key:value pair in dictonary 

marks['harry'] = 89.09 # Updation of value in dictonary

print(marks,type(marks))

# DICT formatting

person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + 'and its marks ' + person['age']

sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age'])

sentence = 'My name is {0} and I am {1} years old'.format(person['name'],person['age'])

print(sentence)

tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)


sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(person,person)

sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)