# python function which converts inches into cms

def InchtoCms(inch):
    cms = inch * 2.54
    return cms

inch = float(input("Enter the inches"))
Cm = InchtoCms(inch)
print(f"{inch} inches into cms is: {Cm}")


# python function which converts cms into inches

def CmstoInch(Cm):
    inch = Cm / 2.54
    return inch

Cm = float(input("Enter the centimeter: "))
inch = CmstoInch(Cm)
print(f"{Cm} inches into cms is: {inch}")