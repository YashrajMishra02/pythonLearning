# Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).

num = int(input("Enter the integer: "))
print(f"Sum or product according to user's choice:\nType 1 to print the sum till {num}th term\nType 2 to print the product till {num}th term")
choi = int(input("Enter the choice: "))

if(choi == 1):
    sum = (num *(num + 1))/2
    sum = int(sum)
    print("The sum of term is: ", sum)
elif(choi == 2):
    i = 1
    pro = 1
    while(i <= num):
        pro *= i
        i += 1
    print("The product of term is: ",pro)