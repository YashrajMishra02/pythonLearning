# Replace "Donkey" with "######" in the file

with open("custom.txt",'r+') as f:
    key = f.read()
    if key[0:6] == 'Donkey':
        f.seek(0)
        f.write("######")
     