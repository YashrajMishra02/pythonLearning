import re

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'[89]\d\d[-.]\d\d\d[-.]\d\d\d\d')

with open('data.txt' , 'r') as f:
    content = f.read() # .read() method read the text file as a string 
    print(type(content))
    matches = pattern.finditer(content)
    print(type(matches)) # here after using finditer() method matches type is <Callable iterator>
    for match in matches:
        print(match)
