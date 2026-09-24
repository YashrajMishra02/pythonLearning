# progarm to print reverse right half pyramic pattern
# ***
# **
# *

# n = int(input("Enter no of rows in reverse right half pyramid star pattern: "))
# for i in range(1,n+1):# or use  for i in range(n,0,-1):
#     for j in range((n+1)-i): #      for j in range(i):
#         print("*", end = "")
#     print()


    # OR

n = int(input("Enter no of rows in reverse right half pyramid star pattern: "))
for i in range(1,n+1):
    print("*" * (n-i+1), end='')
    print()

#               AND

# progarm to print mirror reverse right half pyramid pattern
# ***
#  **
#   *

# n = int(input("Enter no of rows for mirror reverse right half pyramid star pattern: "))
# i = 1
# while(i <= n):
#     j = 1
#     k = 1
#     while(k <= i-1):
#         print(" ", end='')
#         k+=1
#     while(j <= n - i + 1):
#         print("*", end='')
#         j+=1
#     i+=1
#     print()

    # OR

n = int(input("Enter no of rows for mirror reverse right half pyramid star pattern: "))
i = 1
while(i <= n):
    print(" " * (i-1),end='')
    print("*" * (n-i+1))
    i+=1
    