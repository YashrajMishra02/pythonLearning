# Programto find whether a given username contains less than 10 characters or not
user = input("Enter the username: ")
if(len(user)<10):
    print(f"Invalid username: {user} containig less then 10 characters")
else:
    print(f"Valid username: {user}")