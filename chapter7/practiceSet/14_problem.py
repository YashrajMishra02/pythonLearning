# Program to print to check if the given series is increasing or decreasing or not

n = int(input("Enter the number: "))
prev  = int(input("Enter the first number: "))
i = 1
isDec = True
count = 0
while(i < n):
    current = int(input("Enter the next number: "))
    if(prev == current):
        count += 2
        break
    elif(prev < current): # increaisng
        if(isDec == True):
            isDec = False
            count += 1
            prev = current
            i += 1
        else:
            prev = current
            i += 1
    elif(prev>current): # decreasing
        if(isDec == False): # if decresing check if previous it was incerasing or not?
            count += 2
            i += 1
        else:
            prev = current
            i += 1

if(count == 0):
    print("True")
elif(count == 1):
    print("True")
else:
    print("False")
