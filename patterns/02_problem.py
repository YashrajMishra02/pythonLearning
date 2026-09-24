# program to print right half pyramid star pattern 
# *
# **
# ***

n = int(input("Enter no of rows for right half pyramid star pattern: "))
# for i in range(1,n+1):
#     for j in range(0,i):
#         print('*', end = "")
#     print()

    # OR

# n = 5
for i in range(1, n+ 1):
    print("*" * i)

# program to print mirror right half pyramid star pattern 
#   *
#  **
# ***

n = int(input("Enter number of rows for mirror image of above star pattern: "))
for i in range(1,n+1):
    print(" " * (n-i), end='')
    print("*" * i, end='')
    print()
