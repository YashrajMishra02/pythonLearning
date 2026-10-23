

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
    def __init__(self, first, last, pay, employees = None): 
        ''' Passing list of employees as a default argument instead of none 
        BUT *** YOU NEVER WANT TO PASS MUTABLE DATA TYPES like LIST or DICTONARY AS DEFAULT ARGUMENT *** 
        '''
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

print(mgr_1.email)

# mgr_1.print_emps()

mgr_1.add_emp(dev_2)

# mgr_1.print_emps()

mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

