

class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def email(self): 
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self): # every time fullname method come and grab the current full name and lastname
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1  = Employee('viktor','frankl')

emp_1.fullname = 'Panlo Coelho'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
