# find whether a given number is prime or not
num = int(input("Enter a number to check its prime or not: "))

flag = True
for i in range(2,num):
    if(num%i == 0):
        flag = False

if(flag ==  False):
    print(f"{num}, is not a prime number ")
else:
    print(f"{num}, is a prime number ")


# OR
# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not prime")
#         break

# else:
#     print("Number is prime")
