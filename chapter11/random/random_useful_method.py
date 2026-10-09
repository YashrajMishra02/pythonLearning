import random

# randint() method help to inclusively get the integer value between the provided range
value = random.randint(1,6)

greetings = ['Hello','Hi','Hey','Howdy','Hola']
# choice() method helps to pick a value from the list of values
value = random.choice(greetings)
print(value + ', Yashraj')

# choices() method is used to get a multiple random values form the list but the choices is redundant
colors = ['Red','Black','Green','Blue','Yellow','Orange','Voilet','Indigo','White']
result = random.choices(colors,k=10)
result = random.choices(colors,weights=[18,18,4],k=10) # weights=[valuess] help to decide how frequent the value should occur
print(result)

deck =list(range(1,53))
# shuffle() method is use to shuffle the list of values 
random.shuffle(deck)
print(deck)

# sample() method choose the unique value from list without redundancy 
hand = random.sample(colors,k = 5)
print(hand)

