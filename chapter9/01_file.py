# File handling in Python

f = open("file.txt", "+a")
f.write("hehehehehehehe...")
data = f.read()
print(data)
f.close() # always important to close the file