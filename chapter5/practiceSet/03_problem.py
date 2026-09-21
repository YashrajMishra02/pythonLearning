# Can we have a set with 18 (int) and '18' (str) as a value in it?

l = set()
l.add(int(input("Enter number : ")))
l.add((input("Enter number : ")))
print(l)
