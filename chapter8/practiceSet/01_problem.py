# Program using functions to find greatest of three numbers

def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3

n1 = int(input("Enter number"))
n2 = int(input("Enter number"))
n3 = int(input("Enter number"))
# value = 
print(f" The greatest number is: {greatest(n1,n2,n3)}")