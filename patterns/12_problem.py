# Program to print left pascal triangle
'''
*   
**  
*** 
****
*** 
**  
*   
'''

row = int(input("Enter the no of rows for left pascal triangle: "))
# row = row * 2 - 1
i = 1
while(i<=row):
    print("*" * i)
    i += 1
i = row -1
while(i > 0):
    print("*" * i)
    i -= 1

# Program to print right pascal triangle
'''
   *
  **
 ***
****
 ***
  **
   *
'''

row = int(input("Enter the no of rows for right pascal triangle: "))
i = 1
while(i <= row):
    print(" " * (row-i),end='')
    print("*" * i)
    i += 1
i = row - 1
j = 1
while(i>0):
    print(" " * j, end='')
    print("*" * i)
    j += 1
    i -= 1

