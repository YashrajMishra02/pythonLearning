
# problem solving of factoraial using generators

# FACTORAIL USING NAIVE AND GENERATOR

def fact(number):
    ans = 1
    for i in range(1,number + 1):
        ans *= i
    yield ans
num = int(input("enter number: "))
print(next(fact(num)))

# FACTORAIL USING RECURSION AND GENERATOR

def fact(number):
    if number == 1:
        yield 1
    ans = number * next(fact(number - 1))
    yield ans

num = int(input("enter number: "))
print(next(fact(num)))
