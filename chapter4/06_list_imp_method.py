# Program to concatinate two list using extend method

l1 = [2,1,3,9,34,12,45,21]
l2 = ["supper","bappa"]
# l1.append(l2) # This will append the entire list as a single element in list not as individual element into the first list

l1.extend(l2)
print(l1)
print(l1[8])

