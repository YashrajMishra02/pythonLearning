# Program to print the square hollow star pattern
'''
n = 3
* * * 
*   *
* * *
n = 4
* * * *
*     *
*     *
* * * *
n = 5
* * * * *
*       *
*       *
*       *
* * * * *
'''
n = int(input("Enter no of rows in square hollow star pattern: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* " * n, end='')
    else:
        print("* " * 1, end='')
        print("  " * (n-2), end='')
        print("*" * 1, end='')
        
    print()
