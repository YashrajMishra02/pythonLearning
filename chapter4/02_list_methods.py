# Program of every useful list method's

li = [2,1,3,9,34,12,45,21]

print('Original List: ', li)

# sort() method sort the original list in ascending order
li.sort()

print('Original sorted List: ', li)

# Using Sorted function, it returns new list
s_li = sorted(li,reverse=True)

print('Sorted using sorted function: ', s_li)

li.sort(reverse=True) # Another method to reverse the list

li.reverse()

print(li[0:6]) # List sliciing and another string slicing rule apply as well

print(li.index(21)) # Finding value in list with built in index method

li.insert(3,23) # Inserting value in list at particular index 

li.append(82) # Inserting value at the end of the list

li.remove(21) # Removing particular value from list

value  = li.pop(2) # Pop the value from particular index and return the value   
# print(value)

print(li)

li = [-6,-5,-4,3,2,1]

s_li = sorted(li)
print(s_li)

s_li = sorted(li,key=abs)
print(s_li)

# List formatting
l = ['jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(l)

print(sentence)