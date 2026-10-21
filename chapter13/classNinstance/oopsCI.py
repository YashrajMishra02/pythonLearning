
# Python Object-Oriented Programming

class Employee:
    def __init__(self,first,last,pay):
        # first, last, pay are the attributes of the class
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    # Creating method in class
    def fullname(self):
        return (f"{self.first} {self.last}")

emp_1  = Employee('harry','raj',30000)
emp_2 = Employee('cherry','ram',90000)

print(emp_1.pay)
print(emp_2.last)
print(emp_1.fullname()) # This transformed into the Employee.fullname(emp_1) itself 

# Calling class method using class name itself
print(Employee.fullname(emp_2))

# without class need of storing the multiple data of a Single Employee

emp_1.first = 'harry'
emp_1.last = 'raj'
emp_1.pay = 30000
emp_1.email = 'harry02raj@company.com'

emp_2.first = 'cherry'
emp_2.last = 'ram'
emp_2.pay = 90000
emp_2.email = 'cherry22ram@company.com'

print(emp_1.email)
print(emp_2.email)
print(f"{emp_1.first} {emp_1.last}")

