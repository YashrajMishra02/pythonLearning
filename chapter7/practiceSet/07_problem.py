# Program to print multiplication table of n using for loop in reverse order
num = int(input("enter number: "))
for i in range(10,0,-1): # OR for i in range(1,11):
    # print(i)
    print(f"{num} x {i} = {num * i}") # OR print(f"{num} x {11-i} = {num * (11-i)})