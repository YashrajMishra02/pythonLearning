# Program to print multiplication table of given number using for loop
num = int(input("Enter a number to see its table: "))

for i in range(1,11):
    value = num * i
    print(f"{num} x {i} = {value}")