# Program to find sum of first n natural nubmer using while loop
n = int(input("Enter number to find its sum of natural nubmer"))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(f"Sum of {n} number is {sum}")