# Learning about the Nested list compherension 
# syntax 
# new_list = [[expr for item in inner_iterable] for item in outer_iterable]

# Creating a matrix
# without list comprehension 
m = []
for i in range(5):
    m.append([])            # Add empty row
    for j in range(5):
        m[i].append(j)      # Add values 0-4 in each row

print(m)

# with list comprehension 
m = [[c for c in range(5)] for r in range(5)]       # inner loop [c for c in range(5)] create each row and outer loop repeat it 5 times
print(m)