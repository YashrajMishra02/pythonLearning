
# Day 3: Of creating a project for next 50 days
# Topic: Currency conveter

def CrnCon(inCrncy, ouCrncy):
    result = 0
    if ouCrncy == 'usd':
        result = int(inCrncy/94.03)
        return result
    elif ouCrncy == 'pkr':
        result = int(inCrncy*2.96)
        return result
    elif ouCrncy == 'yuan':
        result = int(inCrncy/7.09)
        return result
    elif ouCrncy == 'yen':
        result = int(inCrncy/169.89)
        return result


ipCrncy = int(input("Enter your input currency: "))
opCrncy = input("Enter your convertion currency initial: \n eg:\t usd: us dollor \n\t pkr: pakistan rupees \n\t yuan: chinese rupees \n\t yen: japaness rupees \n\t like that: \t")

print(f"The transformation of {ipCrncy} into {opCrncy} is {CrnCon(ipCrncy, opCrncy)}")
