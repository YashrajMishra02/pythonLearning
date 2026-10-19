# Iterators
nums =[1,2,3]

# To know if it is iterable or not it should conation a  __iter__ method

# To know the list contain the __iter__ method check using dir()
print(dir(nums))

# This line will cause an error as {list are iterable but not an iterator}
print(next(nums))

# Iterable
# Iter method return an iterator but its the same object hence it return it-self
i_nums = nums.__iter__() 
    # OR
i_nums = iter(nums) # it call __iter__ method for the object that's been passed 

# This is an List iterator 
print(i_nums)

# As an iterator it contain both iter() and next() methods 
print(dir(i_nums))

# Iterator has a state through which they know what would be the next value
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

# But if there is no next element / ran out of value it raise stop iteration error
print(next(i_nums))
