# Converting list to string using join method of string
names = ['sam','jay','doremon','zoro','hinata']

print(names)

names_str = ', '.join(names) # Using join method of string

# names_str = ' - '.join(names) # Using join method of string
print(names_str)


# Convert string to list using split method

# new_names = names_str.split(" - ")
new_names = names_str.split(" , ")

print(new_names)
print(new_names[0])