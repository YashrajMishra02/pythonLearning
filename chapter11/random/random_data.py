''' Super simple module to create basic random data for tutorials '''
import random
first_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emma", "Tom", "Lily", "David", "Sophia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson"]
street_names = ["Main St", "Elm St", "Oak St", "Pine St", "Maple St", "Church St", "Broadway", "Park Ave", "Ridge Rd", "Green St"]
fake_cities = ["Oakdale", "Springfield", "Lincoln", "Rochester", "Burlington", "Pittsburgh", "Cincinnati", "Minneapolis", "Sacramento", "Tucson"]
states = ["CA", "NY", "TX", "FL", "IL", "OH", "PA", "GA", "NC", "MI"]

with open('data.txt', 'w') as f:
    for num in range(100):
        first = random.choice(first_names)
        last = random.choice(last_names)
        phone = f"{random.randint(100,999)}-555-{random.randint (1000,9999)}"
        street_num = random.randint(100,999)
        street = random.choice(street_names)
        city = random.choice(fake_cities)
        states = random.choice(states)
        zip_code = random.randint(10000,99999)
        address = f"{street_num} {street} St., {city} {states}  {zip_code}"

        email = first.lower() + last.lower() + '@bogusemail.com'

        print(f"{first} {last}\n{phone}\n{address}\n{email}")
        print()
        f.writelines(f"{first} {last}\n{phone}\n{address}\n{email}\n")
