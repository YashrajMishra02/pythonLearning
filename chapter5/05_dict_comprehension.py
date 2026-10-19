# Learning the Dictonary comprehension

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

print (list(zip(names,heros))) # NOTE by default the zip() cannot be printed as print() by default print the memory address of the object hence convert it into list i.e. list(zip(value,value1))


# I want a dict{'name': 'hero'} for each name,hero in zip(names,heros)
my_dict = {}
for name, hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)


# DICT COMPREHENSION
my_dict = {name: hero for name, hero in zip(names,heros)}
print(my_dict)

# if name not equal to Peter
my_dict = {name: hero for name, hero in zip(names,heros) if name != 'Peter'}
print(my_dict)