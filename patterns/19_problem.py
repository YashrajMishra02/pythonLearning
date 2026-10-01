# Program to print Palindrome Triangular pattern
'''

      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4

'''

row = int(input("Enter the number of row to see Palindrome Traingular pattern: "))

i = 1
while(i<= row):
    print(" " * (row - i), end='')
    j = i
    while(j>0):
        print(j,end='')
        j -= 1
    if(i >=2 and i <= row):
        j = 1
        while(j <= i-1 and j != 0):
            print(j+1,end='')
            j += 1  
        print()
        i += 1
    else:
        print()
        i += 1