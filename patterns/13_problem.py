# Program to print sandglass
# * * * *
#  * * *
#   * *
#    *
#   * *
#  * * *
# * * * *

# row = int(input("Enter the base row to print sandglass: "))
# i = 1
# while(i <= row):
#     j , k = 1 , 1
#     while(k <= i - 1):
#         print(" ", end='')
#         k += 1
#     while(j <= row - i + 1):
#         print("* ", end='')
#         j += 1
#     print()
#     i += 1

# i = 2
# while(i<=row):
#     j = 1
#     while(j <= row - i):
#         print(" ", end='')
#         j += 1
#     print("* " * i)
    # i += 1
                
                # OR

row = int(input("Enter the base row to print sandglass: "))
i = 1
while(i <= row):
    print(" " * (i - 1), end='')
    print("* " * (row - i + 1))
    i += 1

i = 2
while(i<=row):
    print(" "*(row - i), end='')
    print("* " * i)
    i += 1
