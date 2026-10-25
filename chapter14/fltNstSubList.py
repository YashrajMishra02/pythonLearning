
# Flattening Nested Sub-Lists without list comprehension

m = [[1,2,3],[4,5,6],[7,8,9]]
flat = []

for r in m:
    for e in r:
        flat.append(e)

print(flat)


# Flattening Nested Sub-Lists with list comprehension
m = [[1,2,3],[4,5,6],[7,8,9]]
flat = [e for row in m for e in row]
print(flat)
