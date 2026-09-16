a = 10
b = 2

# Arithmetic operator
print("Addition: ",a + b)
print("Subtraction: ",a - b)
print("Multiplication: ",a * b)
print("Division: ",a / b)
print("Floor Division: ",a // b)
print("Modulus: ",a % b)
print("Exponentiation: ", a**2)

# Comparison opeartor
# print(a==b)
# print(a >= b)
# print(b <= a)
# print(a != b)
# print( a>b)
# print( a<b)

# Logical operator
# a = True
# b = False
# print( a and b)
# print( a or b)
# print( not a)

# Assigment opeartor
# a = 3-0.1
# b = 22
# b +=0.1
# a -= 1
# c = 2
# c *= b
# print(a)
# print(b)
# print(c)

# Identity Opeartor = "is" and "is not" are used to check if two value are located on the same part of memory

a = 10
b= 20
c = a
print(a is not b)
print(a is c)

# Membership Operator = "in" and "not in" used to test whether a value or variable is in sequence
x = 20
y = 2
list = [10,20,24,35,49,50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in list):
    print("y is present in list")
else:
    print("y is not present in given list")

# Ternary opeartor 
a, b = 10,23
mim = a if a < b else b
print(b)