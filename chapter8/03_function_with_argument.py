# position arguments
def greet(name, ending):
    print("Good bro: " + name + ending)
    return "done"

def greet1(*name, **ending):
    print(name, ending)

a = greet("zoro ", "bye")
print(a)

# keyword arguments
greet(ending= "tata", name = "jakki")

# default arguments
greet("zoro ", "3x2Y")

# arbitrary arguments
greet1("zoro ", "bye", age=20, city="delhi")
