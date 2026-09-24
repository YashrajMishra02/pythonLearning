# Program to print Butterfly pattern
'''
*     *
**   **
*** ***
*******
*** ***
**   **
*     *
'''

row = int(input("Enter no of row for the start of butterfly pattern: "))
i = 1
while(i <= row):
    print("*" * i, end='')
    con = 2*(row-i)-1
    if(con > 0):
        print(" " * (con), end='')
        print("*" * i, end='')
    elif(con < 0 and i == row):
        print("*" * (i-1),end='')
    print()
    i += 1

i = row - 1
j= 1
while(i > 0):
    print("*" * i, end='')
    print(" " * (2*j-1),end='')
    print("*"* i)
    i-=1
    j+=1
