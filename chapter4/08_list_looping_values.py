# Looping value in list

names = ['sam','jay','doremon','zoro','hinata']

for item in names: # Use of Membership operator along with loop traversal in list
    print(item)

# Enumerate method of finding value along with index

for index, person in enumerate(names): # Enumerate function helps to access the index and value in the list
    print(index, person)