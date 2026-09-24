# Program to print Diamond pattern
#   *
#  * *
# * * *
#  * *
#   *

row = int(input("Enter the no of rows for the diamond pattern: "))
i = 1
while(i <= row):
    print(" " * (row - i),end='')
    print("* " * i)
    i+=1
i = row - 1
j = 1
while(i > 0):
    print(" " * j ,end='')
    print("* " * i)
    j += 1
    i -= 1
