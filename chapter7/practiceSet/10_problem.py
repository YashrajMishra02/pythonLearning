# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

num = int(input("Enter the number and see its reverse: "))
revnum = 0
while(num > 0):
    cal = int(num % 10)
    revnum = revnum * 10 + cal
    num = int(num / 10)
print(revnum)