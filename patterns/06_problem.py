# progarm to print Floyd's traingle pattern
# 1
# 23
# 456

num = int(input("Enter n: "))
val = 1
for i in range(1,num+1):
    for j in range(1, i+1):
        print(val, end=' ')
        val += 1
    print()

    # AND

# pattern to print mirror image of Floyd's traingle pattern
#    1
#   23
#  456

num = int(input("Enter n: "))
val = 1
for i in range(1, num+1):
    for k in range(1, (num+1)-i):
        print(" ", end=' ')
    for j in range(1, i+1):
        print(val, end=' ')
        val += 1
    print()