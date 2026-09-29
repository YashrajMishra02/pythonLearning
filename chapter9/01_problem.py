# Check if the word "twinkle" is present in the poem

f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("Word twinkle is present")
else:
    print("Word twinkle is not present")
    



# with open("poem.txt","+a") as f:
#     content= f.readline()
#     if ("twinkle" in content):
#         print("yes it conatins")
#     else:
#         print("no it doesn't conatins")