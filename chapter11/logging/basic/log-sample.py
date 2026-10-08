
import logging


# DEBUG: Detialed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happend, or indicative of some problem in the near future (e.e. 'disk space low). The software is still working as expected.

# ERROR: Due to a more serious proble, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(level=logging.DEBUG) # Way of changing the logging level 

# Altering the default logging i.e. Warning
logging.basicConfig(filename='test.log', level=logging.DEBUG)

# Altering the default logging i.e. Warning along with format 
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x,y):
    """ Add Function """
    return x + y

def subtract(x,y):
    """ Subtract Function """
    return x - y

def multiply(x,y):
    """ Multiply Function """
    return x * y

def divide(x,y):
    """ Divice Function """
    return x/y

num_1 = 20
num_2 = 10


# ADDITION 
add_result = add(num_1,num_2)
print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result)) #this statement will do nothing as default is warning and it will invoke warning and above

logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))


# SUBTRACTION
sub_result = subtract(num_1,num_2)
print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result)) #this statement will do nothing as default is warning and it will invoke warning and above

logging.warning('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))


# MULTIPLICATION
mul_result = multiply(num_1,num_2)
print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result)) #this statement will do nothing as default is warning and it will invoke warning and above

logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))


# DIVISION
div_result = divide(num_1,num_2)
print('Div: {} / {} = {}'.format(num_1, num_2, div_result))

logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result)) #this statement will do nothing as default is warning and it will invoke warning and above

logging.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))

logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

