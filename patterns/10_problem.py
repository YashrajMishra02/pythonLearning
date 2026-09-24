# Program to print isoceles triangle
#    1
#   121
#  12321
# 1234321

n = int(input("Enter the no of rows for isoceles triangle: "))
i = 1
while(i <= n):
    print(" " * (n - i), end='')
    j = 1
    while(j <= i):
        print(j, end='')
        j += 1
    j = i - 1
    while(j >= 1):
        print(j, end='')
        j -= 1
    print()
    i += 1


# Program to print inverted isoceles triangle
# 1234321
#  12321
#   121
#    1


n = int(input("Enter the no of rows for inverted isoceles triangle: "))
i = 1
j = 1
while(i<=n):
    j = 1
    while(j < i):
        print(" ", end='')
        j += 1
    k = 1
    while(k <= n-i+1):
        print(k, end='')
        k += 1
    a = n - i
    while(a > 0):
        print(a, end='')
        a -= 1
    print()
    i+=1