# Program : Given a binary number as an integer N, convert it into decimal and print.

num = int(input("Enter the binary number to know its decimal number: "))
i  = 0
interm = 0
while(num > 0):
    sol = int(num % 10)
    if(sol == 1 or sol == 0):
        interm = interm + sol * (2**i)
        i+=1
    num = int(num/10)

print(interm)
