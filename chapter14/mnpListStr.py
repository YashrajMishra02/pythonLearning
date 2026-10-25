
# Manipulate String without list comprehension


m = [["apple", "banana", "cherry"],
     ["date", "fig", "grape"],
     ["kiwi", "lemon", "mango"]]

mod_m = []
for r in m:
    mod_r = []
    for f in r:
        mod_r.append(f.capitalize())
    mod_m.append(mod_r)
print(mod_m)


# Manipulate String Using List Comprehension

m = [["apple", "banana", "cherry"],
     ["date", "fig", "grape"],
     ["kiwi", "lemon", "mango"]]

mod_m =[[value.capitalize() for value in row] for row in m]
print(mod_m)