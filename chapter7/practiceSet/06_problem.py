# Program to calculate the factorail of given number using for loop
n = int(input("Enter number to find its factorail: "))
fac = 1
for i in range(1,n+1):
    fac *= i
print("factoraiol is :", fac)