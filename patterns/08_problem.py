# Program to print continous number pattern
num = int(input("Enter no of rows to print continous number pattern: "))
i = 1
while(i <= num):
    j = i
    while(j >= 1):
        print(j, end='')
        j -= 1
    print()
    i += 1



# Program to print mirror of continous number pattern
#   1
#  12
# 123

num = int(input("Enter no of row to print mirror of continous number pattern: "))
i = 1
while(i <= num):
    j = 1
    k = 1
    print(" " * (num - i), end='')
    while(j <= i):
        print(j, end='')
        j += 1
    print()
    i += 1
