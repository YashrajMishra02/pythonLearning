# Program to find the first n terms of the series 3N + 2 which are not multiples of 4
n = int(input("Enter the no of term you want to find that are not multiple of 3N + 2: "))
i = 1
list = []
while(len(list) != n):
    count = 3*i + 2
    if(count%4 != 0):
        list.append(count)
    i += 1
print(list)