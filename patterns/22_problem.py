# Program to print Reverse Number Traingle Pattern
'''

1 2 3 4 
 2 3 4
  3 4
   4

'''

row = int(input("Enter the no of row to print Reverse Number Triangle Pattern: "))
i = 1
while(i <= row):
    print(" " * (i-1),end='')
    j = i
    while(j <= row):
        print(f"{j} ", end='')
        j += 1
    print()
    i += 1