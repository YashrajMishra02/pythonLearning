# Replace "Donkey" with "####" in the file

with open("myfile.txt","+a") as f:
    f.write("use of with statement in python")
    data = f.read()
    print(data)
    