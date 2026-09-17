#  Program to detect double space in a string.

word = input("Enter any thing:  ")
print(word.find("  "))
word.replace('  ', ' ')
print(word) 