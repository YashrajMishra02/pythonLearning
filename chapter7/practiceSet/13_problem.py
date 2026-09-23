# Given a number N, find its square root. You need to find and print only the integral part of square root of N.

num = int(input("Enter the number to know its square root: "))
i = 1
while(i <= num):
    if(i*i == num):
        print(i)
        break
    elif(i*i < num):
        i += 1
    else:
        print("the integral part of square root of", num, "is", i-1)
        break
