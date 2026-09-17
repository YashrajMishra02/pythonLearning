# Program to fill in a letter template given below with name and date
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

name = input("Enter your Name:\n")
date = input("Enter today's date:\n")
letter = f'''Dear {name} \nYou are selected!\n{date}'''
letter = ''' Dear <|name|>
You are selected!
<|date|>'''

# chaining of functions with predefined string
print(letter.replace("<|name|>", {"Yashraj"}).replace("<|date|>", "07 september 2026"))