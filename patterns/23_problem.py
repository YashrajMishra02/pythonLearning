# Program to print Mirror Image Triangle Pattern
'''

1 2 3 4
 2 3 4
  3 4
   4
  3 4 
 2 3 4 
1 2 3 4 

'''

row = int(input("Enter the no of row to print the Mirror Image Traingle Pattern: "))
i = 1
while(i <= row):
    print(" "*(i-1),end='')
    j = i
    while(j <= row):
        print(f"{j} ",end='')
        j += 1
    print()
    i += 1
i = 2
while(i<= row):
    print(" " * (row -i),end='')
    j = row - i + 1
    while(j <= row):
        print(f"{j} ", end='')
        j += 1
    print()
    i += 1