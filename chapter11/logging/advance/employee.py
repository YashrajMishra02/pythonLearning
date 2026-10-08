import logging

# Logger variable
logger = logging.getLogger(__name__)

# setting logger level
logger.setLevel(logging.INFO)

# formating will be to the file_handler not the logger
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# Defining where to log 
file_handler = logging.FileHandler('employee.log')

# Setting the format of the file in which the data should be logged 
file_handler.setFormatter(formatter)

# once file has been decided now to add with the logger
logger.addHandler(file_handler)


'''logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(name)s:%(message)s')
'''
class Employee:
    """ A sample Employee Class """

    def __init__(self,first,last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        # logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Lal', 'baugh')
emp_3 = Employee('yashraj','mishra')