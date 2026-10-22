
# Class Methods

class Employee:

    # class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        # first, last, pay are the attributes of the class
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1
    # Creating method in class
    def fullname(self):
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # OR 
    #   self.pay = int(self.pay * Employee.raise_amount)

    @classmethod # --> decoarator 
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp_1  = Employee('harry','raj',30000)
emp_2 = Employee('cherry','ram',90000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.05) 

        # OR
        
emp_1.set_raise_amt(1.05) # This will also work but it is not recommended to use class method with instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

