# File handling in Python
# Naive method to open a file and write to it

f = open("file.txt", "+a")
f.write("hehehehehehehe...")
data = f.read()
print(data)
f.close() # always important to close the file