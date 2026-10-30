
#  learning generator : generator don't hold the entire result (i.e the actual value) in memory it yeilds one result at time

def square_number(nums):
    for i in nums:
        yield (i*i)

my_nums = square_number([1,2,3,4,5])

# using list comprehension to get the value from the generator object

print (my_nums) # this line will return the generator object number not the value


print(next(my_nums)) # this line will return the value one by one
print(next(my_nums)) 
print(next(my_nums)) 
print(next(my_nums)) 
print(next(my_nums)) 


for num in my_nums:
    print(num) # this line will return the value one by one
