
# Class Variables: A Variable that can be accessed by all the instance of the instance variable

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

print(Employee.num_of_emps)

emp_1  = Employee('harry','raj',30000)
emp_2 = Employee('cherry','ram',90000)

print(Employee.num_of_emps)
print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)

# Accessing the class variable through instance variable, class 
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

# Printing out the namespaces of the instance and class
print(emp_1.__dict__)
print()
print(Employee.__dict__)
print()
print(emp_2.__dict__)

# Employee.raise_amount = 1.05

# The below line create a new attribute inside the employee1 instance and update the raiseamount for specific instance 
emp_1.raise_amount = 1.05

print(emp_1.__dict__)
print()
print(Employee.__dict__)
print()
print(emp_2.__dict__)

# Updating the class variable 
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

# Printing the namespace of instance varaible and class
print(emp_1.__dict__)
print()
print(Employee.__dict__)

