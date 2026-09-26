# Program of every useful list method's

l1 = [2,1,3,9,34,12,45,21]
print(l1)

l1.sort() # Sort the list in ascending order

l1.sort(reverse=True) # Another method to reverse the list

l1.reverse()

print(l1[0:6]) # List sliciing and another string slicing rule apply as well

print(l1.index(21)) # Finding value in list with built in index method

l1.insert(3,23) # Inserting value in list at particular index 

l1.append(82) # Inserting value at the end of the list

l1.remove(21) # Removing particular value from list

value  = l1.pop(2) # Pop the value from particular index and return the value   
print(value)

print(l1)


