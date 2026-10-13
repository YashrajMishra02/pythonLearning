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

sentence = 'Start a sentence and then bring it to an end'

print('\tTab') # Normal string
print(r'\tTab') # r string

pattern = re.compile(r'abc') # re.compile('pattern') allows you to seperate the pattern into 

pattern = re.compile(r'bca') # its a case sensitive

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # here period operator i.e. (.) can uses any character
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattern = re.compile(r'[a-zA-Z]')
pattern = re.compile(r'[^a-z]')
pattern = re.compile(r'[^b]at')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')


pattern = re.compile(r'\.') # for the special character use 

# backslash i.e. for {.} use {\.}

pattern = re.compile(r'coreyms\.com') # for the special character use backslash i.e. for {.} use {\.}

matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)

for match in matches:
    print(match)


