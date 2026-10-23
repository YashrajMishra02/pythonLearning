

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

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # this passes the first, last, pay to our employee class init method, also helpful in single inheritance allows us to maintain
        # Employee.__inti__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None): # passing list of employees
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1  = Developer('harry','raj',50000, 'python')
dev_2 = Developer('cherry','ram',70000, 'java')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])

# isinstance() CHECK if the object is the instance of the class

print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False


# issubclass() CHECK if the class is the subclass of other 

print(issubclass(Manager, Employee)) # True because Employee is the parent class of Manager
print(issubclass(Manager, Developer)) # False because Developer is not the parent class of Manager

