
#  Build BankAccount class: deposit, withdraw, balance, overdraft protection. Add __str__, __repr__, __eq__ magic methods.

# deposit == entering the amount to be deposited
# withdraw amount to be withdrawm from the account
# balance to check the balance of the user 
# add __str__ method
# add __repr__ method

class BankAccount:
    def __init__(self, deposit, withdraw, status):
        if status == "new":
            self.balance = 0
        else:
            self.balance = 10000

        self.deposit = deposit
        self.balance += deposit
        self.wdraw = withdraw

    def wdrw(self):
        self.balance -= self.wdraw
        return f"After withdraw of amount {self.wdraw} balance is {self.balance}"

    def __repr__(self):
        return f"Deposited: {self.deposit}, Balance after deposit & withdrawl of money: {self.balance} withdrawl amount {self.wdraw}"


    def __str__(self):
        return f"Amount {self.deposit} deposited successfully your balance account is {self.balance} with {self.wdraw} as withdraw amount"


status = input("Enter your status i.e. new or old: ")
dpAmt = int(input("Enter the deposit amount: "))
wdAmt = int(input("Enter the withdraw amount: "))

if status == 'new':
    user_1 = BankAccount(dpAmt, wdAmt, status)
    if wdAmt != 0:
        print(user_1.wdrw())
    print(repr(user_1))
    print(str(user_1))
elif status == 'old':
    user_2 = BankAccount(dpAmt, wdAmt, status)
    if wdAmt != 0:
        print(user_2.wdrw())
    print(str(user_2))
else:
    print("invalid status")