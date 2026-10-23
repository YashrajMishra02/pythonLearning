
# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes.

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

class Developer(Employee):
    raise_amount = 1.10 # MORE COMPLEX CHANGES 
    pass

emp_1  = Employee('harry','raj',30000)
emp_2 = Employee('cherry','ram',90000)
print(emp_1.pay)
print(emp_2.email)


    # OR    

# subclass inherit's the methods and attributes of the parent class

dev_1  = Developer('harry','raj',50000)
# dev_1  = Employee('harry','raj',50000)
dev_2 = Developer('cherry','ram',90000)
print(dev_1.pay)
print(dev_2.first)

# help() function help's to visualise easily how python finds the executable methods and attributes in the class, how it flow through out the subclasses > classes > built in functions
# METHOD RESOLUTION ORDER (MRO) is the order in which python looks for the methods and attributes in the class, subclasses, built in functions
print(help(Developer))

#           CUSTOMIZATION

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

