
# customizing the __add__() method for our object

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

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    
emp_1  = Employee('harry','raj',50000)
emp_2 = Employee('cherry','ram',90000)

# Indirectly calling this methods 
print(emp_1.__repr__())
print(emp_1.__str__()) 

print(emp_1 + emp_2)


# len method
print(len('name'))

print('name'.__len__())

print(emp_1.fullname())
print(emp_1.__len__())