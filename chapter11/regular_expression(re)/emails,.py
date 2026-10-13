import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
# here "@" is like a uppercircuit that tells find the pattern until it hit the @ symbol
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)