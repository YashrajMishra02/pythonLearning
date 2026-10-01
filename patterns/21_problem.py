# Program to print the K pattern
'''

* * * *
* * *
* *
*
* *
* * *
* * * *

'''

row = int(input("Enter the no of row for the K Pattern: "))
i = 1
while(i <= row):
    print("* " * (row - i + 1))
    i += 1
i = 2
while(i <= row):
    print("* " * i)
    i += 1