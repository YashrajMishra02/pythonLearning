import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
bat
rat
mat
pat 

'''
sentence = 'Start a sentence and then bring it to an sentence end'

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'sentence') 

matches = pattern.finditer(text_to_search) # return match object with start and end index of the match

matches = pattern.findall(text_to_search) # return only group for the back reference and if multiple group there then it return tuples 

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)

matches = pattern.match(sentence)

matches = pattern.search(sentence)

# FLAGS USAGE
# Normally without use of flag we have to check if it matches the combaniation
pattern = re.compile(r'[Ss][Tt][Aa][Rr][Tt]')

# the re.IGNORECASE flag help to ignore this 
pattern = re.compile(r'SenTence', re.IGNORECASE) # OR re.I works same
matches = pattern.search(sentence)

print(matches)

