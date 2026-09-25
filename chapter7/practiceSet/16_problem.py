# Program to print all the prime number till the given number
num = int(input("Find all the prime number till given number: "))
i = 2
while(i < num):
    j = 2
    while(j <= i):
        if(i==j):
            print(f"{i} ", end='')
            j+=1
            continue
        elif(i%j == 0):
            break
        j+=1
    i+=1
        
