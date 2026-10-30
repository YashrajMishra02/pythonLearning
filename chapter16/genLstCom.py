# using list comprehension to get the value from the generator object

my_nums = [num*num for num in [1,2,3,4,5]]

print(my_nums) # this line will return the value in list format

# Hence to convert my_nums list into generator we will use () instead of [] in the list comperhension i.e.

for num in my_nums:
    print(num) # this line will return the value one by one

# generator comprehension has been created using () instead of [] in the list comprehension i.e.
my_nums = (num*num for num in [1,2,3,4,5])

print(my_nums) # this line will return the value in generator object format

for num in my_nums:
    print(num) # this line will return the value one by one

# converting the generator object into list using list() function
print(list(my_nums)) # this line will return the value in list but its not useful because we loose the advantage of generator i.e. memory efficient because it will hold the entire result in memory