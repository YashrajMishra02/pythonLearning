tup = (2,5,6,False,1,23,1,4,1)

# Sort the tuple
s_tup = sorted(tup)

print(s_tup)

print(tup.count(1)) # count the number of times a value appears in tuple

print(tup.index(1)) # find the index of the first occurrence of a value in tuple

repeated = tup *3

print(repeated)

# membership operator     
print(2 in tup) # check if a value is in the tuple
print(34 in tup) # check if a value is in the tuple