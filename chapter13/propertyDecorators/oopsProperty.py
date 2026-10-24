

class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

        # self.email = self.first + '.' + self.last + '@company.com' # --> doing like that won't update the email using current first/last name 

    @property
    def email(self): 
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def fullname(self): # every time fullname method come and grab the current full name and lastname
        return f"{self.first} {self.last}"
    

emp_1  = Employee('viktor','frankl')

emp_1.first = 'John'

print(emp_1.first)

# print(emp_1.email())

# Inorder to keep accesing the email as an attribute instead of accessing as a method using PROPERTY Decorator as a GETTER
print(emp_1.email)
# print(emp_1.fullname())
print(emp_1.fullname)