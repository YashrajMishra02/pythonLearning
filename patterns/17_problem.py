# Program to print Number increasing reverse pyramid

'''
1 2 3 4
1 2 3
1 2
1
'''

row = int(input("Enter no of row to print number increasing reverse pyramid: "))
i = 1
while(i <= row):
    j = 1
    while(j <= (row-i+1)):
        print(j,end='')
        j += 1
    print()
    i += 1