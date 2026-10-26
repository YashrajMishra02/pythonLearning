

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
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}',{self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"


emp_1  = Employee('harry','raj',50000)
emp_2 = Employee('cherry','ram',90000)

print(emp_1) # printing directly cause it to print vauge values unable to understand

print(repr(emp_1))
print(str(emp_1))

# Indirectly calling this methods 
print(emp_1.__repr__())
print(emp_1.__str__()) 

# OTHER Special Methods for Arithmetic
print(1 + 2) # using special method --v
print(int.__add__(1,2)) # --> is the actual call of the method
print(str.__add__('a', 'b')) # --> This method is for string

