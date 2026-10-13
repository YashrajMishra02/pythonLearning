import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
print(type(pattern))

# Use Group to capture information from url
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# create group[0] containing all the pattern 



matches = pattern.finditer(urls)

for match in matches:
    print(match)
    pass
