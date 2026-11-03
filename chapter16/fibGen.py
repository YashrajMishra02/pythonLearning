
# FIBONNACI USING RECURSION AND GENERATOR

def fib(number):
    if number == 0:
        yield 0
    if number == 1:
        yield 1
    smlAns = next(fib(number-1)) + next(fib(number-2))
    yield smlAns

num = int(input("Enter fibonnaci index to know value of: "))
print(next(fib(num)))