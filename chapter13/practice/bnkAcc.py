
#  Build BankAccount class: deposit, withdraw, balance, overdraft protection. Add __str__, __repr__, __eq__ magic methods.

# deposit == entering the amount to be deposited
# withdraw amount to be withdrawm from the account
# balance to check the balance of the user 
# overdraft protection 
# add __str__ method
# add __repr__ method

class BankAccount:
    def __init__(self, deposit, withdraw, status, overdraftAmt):
        if status == "new":
            self.balance = 0
        else:
            self.balance = 10000

        self.deposit = deposit
        self.balance += deposit
        self.wdraw = withdraw
        self.overdraft = overdraftAmt

    # use of 
    @property
    def wdrw(self):
        self.balance -= self.wdraw
        if self.balance < 0:
            self.balance += self.overdraft
            print( f"After withdraw of amount {self.wdraw} balance uses overdraft value {self.balance}")
        # return f"After withdraw of amount {self.wdraw} balance is {self.balance}"

    def __repr__(self):
        return f"Deposited: {self.deposit}, Balance after deposit & withdrawl of money: {self.balance} withdrawl amount {self.wdraw}"


    def __str__(self):
        return f"Amount {self.deposit} deposited successfully your balance account is {self.balance} with {self.wdraw} as withdraw amount"


status = input("Enter your status i.e. new or old: ")
dpAmt = int(input("Enter the deposit amount: "))
wdAmt = int(input("Enter the withdraw amount: "))
odpAmt = int(input("Enter the overdraft protection account amount:"))

if status == 'new':
    user_1 = BankAccount(dpAmt, wdAmt, status, odpAmt)
    if wdAmt != 0:
        user_1.wdrw
    print(repr(user_1))
    print(str(user_1))

elif status == 'old':
    user_2 = BankAccount(dpAmt, wdAmt, status)
    if wdAmt != 0:
        user_2.wdrw
    print(str(user_2))

else:
    print("invalid status")