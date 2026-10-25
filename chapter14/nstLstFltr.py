# Filtering nested list 
m = [[1,2,3],[4,5,6],[7,8,9]]
odd = []
for r in m:
    for e in r:
        if e % 2 != 0:
            odd.append(e)

print(odd)


# Filtering nested list using list compherension 
m = [[1,2,3],[4,5,6],[7,8,9]]
# odd = [[[[odd.append(e)] if e % 2 != 0] for e in r]for r in m]
odd = [e for r in m for e in r if e % 2 != 0]
print(odd)