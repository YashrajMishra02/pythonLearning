# Program to print the Rhombus pattern
'''
* * * *
 * * * *
  * * * *
   * * * *
'''
row = int(input("Enter the no of rows to print Rhombus Pattern: "))
i = 1
while(i <= row):
    print(" " * (i - 1),end='')
    print("* " * row)
    i += 1