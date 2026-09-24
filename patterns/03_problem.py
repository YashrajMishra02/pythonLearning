# Program to print full pyramid star patter for n = 3
     
'''
for n = 3 pyramid star pattern 
  *
 ***
*****
'''

# num = int(input("Enter n: "))
# for i in range(1,num+1):
#     for j in range(1, (num+1)-i):
#         print(' ', end='')
#     for k in range(1, i*2):
#         print("*", end='')
#     print()

                  # OR

# n = int(input("Enter number of rows in full pyramid star pattern: "))
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("*" * (2*i-1),end="")
#     print()

                  # OR

'''
for n = 3 pyramid star pattern 
  *
 * *
* * *
'''

num = int(input("Enter n: "))
for i in range(1,num+1):
    print(' ' *(num-i), end='')
    print("* "* i, end='')
    print()

                      # AND

'''
for n = 3 pyramid star pattern 
*****
 ***
  *
'''

# Program to print full Inverted pyramid star patter for n = 3
# n = int(input("Enter number of rows in inverted pyramid star pattern: "))
# i = 1
# while(i <= n):
#     print(" " * (i-1), end='')
#     print("*" *(2 * (n-i)+1))
#     i+=1

'''
for n = 3 pyramid star pattern 
* * *
 * *
  *
'''

n = int(input("Enter number of rows in inverted pyramid star pattern: "))
i = 1
while(i <= n):
    print(" " * (i-1), end='')
    print("* " * (n - i + 1))
    i+=1


