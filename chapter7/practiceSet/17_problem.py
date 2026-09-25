'''
Write a program to count and print the total number of characters (lowercase english alphabets only), digits (0 to 9) and white spaces (single space, tab i.e. '\t' and newline i.e. '\n') entered till '$'.
That is, input will be a stream of characters and you need to consider all the characters which are entered till '$'.
Print count of characters, count of digits and count of white spaces respectively (separated by space).
'''

str = input("Enter the string: ")
count_of_char = 0
count_of_digit = 0
count_of_whitespace = 0

for ch in str:
    if ch == "$":
        break
    if "a" <= ch <= "z":
        count_of_char += 1
    elif "0" <= ch <= "9":
        count_of_digit += 1
    elif ch == " " or ch == "\t" or ch == "\n":
        count_of_whitespace += 1

print(count_of_char, count_of_digit, count_of_whitespace)