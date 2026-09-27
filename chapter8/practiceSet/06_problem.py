# Program to remove a given word from a list and strip it at the same time

def RmvL(list,name):
    n = []
    for item in list:
        if not(item == name):
            n.append(item.strip(name))
    return n

list = ["rohan", "satyan", "anuty", "uncle","chetan","jay","an"]
print(list)
name = input("Enter the name you want to remove: ")
lnew = RmvL(list,name)
print(lnew)
