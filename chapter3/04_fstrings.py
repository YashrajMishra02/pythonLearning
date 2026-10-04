first_name = 'Kedar'
last_name = 'Nath'

# Traditional format
sentence = 'This is the place {} {}'.format(first_name,last_name)
print(sentence)

# Fstring 
sentence = f"This is the place {first_name}{last_name}"
print(sentence)

# Fstring direct method use in the {}
sentence = f"This is the place {first_name.capitalize()}{last_name.lower()}"
print(sentence)


# Dictonary using Fstring
person = {'name':'Jenn', 'age':23}

# Using Traditional Format
sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age']) 
print(sentence)

# Using Fstring with the string methods
sentence = f"My name is {(person['name']).upper()} and I am {person['age']} years old"
print(sentence)

# CALCULATION
calculation = f'7 times 8 is equal to {7 * 8}'
print(calculation)

# ADVANCED FORMATTING PADDING
for n in range(1,11):
    sentence = f'The value is {n:02}'
    print(sentence)

# FLOATING POINT PRECISION
pi = 3.145922565
sentence = f'Pi is equal to {pi:.5f}'
print(sentence)

# DATETIME and FORMATING
from datetime import datetime

birthday = datetime(1990,1,1)
# sentence = f'Jenn has a birthday on {birthday}'
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)