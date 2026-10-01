# Program to print zero-one triangle
'''
1
0 1
1 0 1
0 1 0 1

'''



row = int(input("Enter no of row to print zero-one triangle: "))
i = 1
while(i <= row):
    if(i % 2 == 0):
        j = 0
        while(j < i):
            if(j % 2 != 0):
                print('1',end='')
            elif(j % 2 == 0):
                print('0',end='')
            j += 1
        print()
        i += 1
    else:
        j = 0
        while(j < i):
            if(j % 2 != 0):
                print('0',end='')
            elif(j % 2 == 0):
                print('1',end='')
            j += 1
        print()
        i += 1
