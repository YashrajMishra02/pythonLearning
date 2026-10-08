
import logging
import employee

# Logger variable
logger = logging.getLogger(__name__)

# setting logger level
logger.setLevel(logging.DEBUG)

# formating will be to the file_handler not the logger
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# Defining where to log 
file_handler = logging.FileHandler('sample.log')

# want to set log level of sample file so that only particular level visible 
file_handler.setLevel(logging.ERROR)

# Setting the format of the file in which the data should be logged 
file_handler.setFormatter(formatter)

# allows to handle the require logging to show on console
stream_handler = logging.StreamHandler()
# no need to have a specific logging level as it is already initialized to the 
stream_handler.setFormatter(formatter)

# once file has been decided now to add with the logger
logger.addHandler(file_handler)

logger.addHandler(stream_handler)

# Altering the default logging i.e. Warning
# logging.basicConfig(filename='test.log', level=logging.DEBUG)

# Altering the default logging i.e. Warning along with format 
'''logging.basicConfig(filename='sample.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')'''

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
    # return x/y
    try:
        result = x/y
    except ZeroDivisionError:
        logger.error("Tried to divide by zero ")

        # it allows you to trace back to the error
        logger.exception("Tried to divide by zero ")
    else:
        return result
num_1 = 20
num_2 = 0

# ADDITION 
add_result = add(num_1,num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result)) #this statement will do nothing as default is warning and it will invoke warning and above

# logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))




# SUBTRACTION
sub_result = subtract(num_1,num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result)) #this statement will do nothing as default is warning and it will invoke warning and above

# logging.warning('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))




# MULTIPLICATION
mul_result = multiply(num_1,num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result)) #this statement will do nothing as default is warning and it will invoke warning and above

# logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))




# DIVISION
div_result = divide(num_1,num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))

# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result)) #this statement will do nothing as default is warning and it will invoke warning and above

# logging.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))

# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))





