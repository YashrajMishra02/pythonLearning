# program to find the greatest of four numbers entered by the user
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))
greatest = n1
if(greatest<n2):
    greatest=n2
else:
    if(greatest<n3):
        greatest = n3
    else:
        greatest = n4

print(f"the greatest number is {greatest}")
