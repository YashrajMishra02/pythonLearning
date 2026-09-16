# Split function functionality
a , b = input("Enter the value: ").split()
print(type(int(a)))
print(type(b))


# input with custom delimiters 
a , b = int, input("Enter the value: ").split(",")
print(a, b)
print(type(a))
print(type(b))