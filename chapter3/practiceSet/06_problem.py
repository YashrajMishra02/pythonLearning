# check permutation of two strings
from collections import Counter
def ispermutation(str1, str2):
    return Counter(str1) == Counter(str2)

str1 = input("Enter a string: ")
str2 = input("Enter a string: ")

print(f"{ispermutation(str1, str2)} it is permutation of each other")