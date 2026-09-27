# Program to find the sum of first n natural numbers using recursion

def nat(n):
    if(n==1):
        return 1
    smalloutput = n + nat(n-1)
    return smalloutput

num = int(input("Enter the number to find it's first n natural number: "))
print(f"Sum of {num} natural is {nat(num)}")