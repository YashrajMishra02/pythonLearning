# Program using function to convert Celsius to Fahrenheit

def CtoF(c):
    fah = c *(9/5) + 32
    return fah

cel = float(input("Enter the celsius to convert into fahrenheit: "))
print(f"Celsius {cel} into fahrenheit is {CtoF(cel)}")


# Program using function to convert Fahrenheit to Celsius

def FtoC(fah):
    cel = (fah -32)*(5/9)
    return cel

fah = float(input("Enter the fahrenheit to convert into celsius: "))
print(f"fahrenheit {fah} into celsius is {FtoC(fah)}")