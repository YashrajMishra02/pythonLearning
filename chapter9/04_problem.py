# Replace "Donkey" with "####" in the file

with open("custom.txt",'+a') as f:
    list = []
    while(f.read() != ""):
        list.append(f.read())
    print(list)
    txt = f.read()
    if ("Donkey" in txt):
        f.write("####")
        