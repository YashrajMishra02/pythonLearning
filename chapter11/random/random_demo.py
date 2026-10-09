import random

# random method randomize the value [0: 1)
value = random.random() 
print(value)

# uniform method randomly give value between the provided range
value = random.uniform(1,10)
print(value) # give random floating point value between the reange
print(int(value)) # to convert the random floating point value to the integer 

