
# Day 1: Of creating a project for next 50 days
# Topic: A number converter(binary, octal, hexadecimal, custom base)

def printer(stack):
    print(len(stack))
    while len(stack) != 0:
        print(stack.pop(),end='')
    
def converter(number, type, numberSystem=10):
    if type == numberSystem:
        print(f"The converted number is : {number}")
    elif type == 2 or 8 or 16:
        stk = []
        quotient = int(number/type)
        remainder = int(number%type)
        while (quotient != 0):
            if (remainder >= 10 and remainder < 16 ):
                dick = {10: 'A', 11: 'B', 12: 'C', 14: 'D', 15: 'E'}
                for item in dick:
                    if item == remainder:
                        stk.append(dick[item])
            else:
                stk.append(remainder)
            number = quotient
            quotient = int(number/type)
            remainder = int(number%type)
        stk.append(remainder)
        printer(stk)


numberInput = int(input("Enter the number: "))

convertType = int(input("Enter the system in which you want to get it converted in: \n" 
"for binary - 2 \n" 
"for octal - 8 \n" 
"for hexadecimal - 16 \n" 
"for any custom base- type number it self: "))

converter(numberInput, convertType)
