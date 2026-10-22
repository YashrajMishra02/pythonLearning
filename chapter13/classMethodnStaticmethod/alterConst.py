
# Alternative Constructors

class Employee:
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1  = Employee('harry','raj',30000)
emp_2 = Employee('cherry','ram',90000)

emp_str_1 = 'harry-raj-30000'
emp_str_2 = 'cherry-ram-90000'

# Brute force method:

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

first, last, pay = emp_str_2.split('-')
new_emp_2 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_2.pay)

# using Alternative Constructor as a method
emp_str_1 = 'harry-raj-30000'
new_emp_1 = Employee.from_string(emp_str_1) # This will create a new instance of the class Employee

new_emp_2 = Employee.from_string('cherry-ram-90000')

print(new_emp_1.email)
print(new_emp_2.pay)