# Program to print adjacent number with half triangle
# 1
# 23
# 345
# 4567

num = int(input("Enter n: "))
for i in range(1,num+1):
    val = i
    for j in range(1, i+1):
        print(val, end='')
        val += 1 
    print()

        # OR

# Program to print mirror image of adjacent number with half triangle
#    1
#   23
#  345
# 4567


num = int(input("Enter n: "))
i = 1
while(i <= num):
    print(" " * (num - i), end='')
    val = i
    j = 1
    while(j <= i):
        print(val, end='')
        j+=1
        val+=1
    print()
    i += 1