# Program to print Number increasing pyramid pattern
# 1
# 12
# 123

num = int(input("Enter no or row for Number increasing pyramid pattern: "))
i = 1
while(i <= num):
    j = 1
    while(j <= i):
        print(j, end='')
        j+=1
    print()
    i+=1

            # OR

# Program to print mirror of number increasing pyramid pattern
#   1
#  21
# 321



num = int(input("Enter no or row for mirror number increasing pyramid pattern: "))
i = 1
while(i <= num):
    j = i
    k = 1
    print(" " * (num - i), end='')
    while(j >= 1):
        print(j, end='')
        j -= 1
    print()
    i += 1