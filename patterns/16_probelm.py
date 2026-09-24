# program to print number triangular pattern
'''
   1
  2 2
 3 3 3
4 4 4 4
'''

row = int(input("Enter the no of row for number traingluar pattern: "))
i = 1
while(i <= row):
    print(" " * (row -i), end='')
    print(f"{i} " * i)
    i += 1