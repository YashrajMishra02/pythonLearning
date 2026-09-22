# program which finds out whether a given name is present in list or not
list = ["rita","yashraj","akash","chetna","sonali"]
check = input("Enter a name which you have to find in the database: ")
if(check in list):
    print(f"Name: {check} found in the database!")
else:
    print(f"Your given name: {check} not found in the database!")