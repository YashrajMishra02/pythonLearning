# speak() — inheritance-based
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# move() — duck typing (no shared parent)
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

# Both work the same way polymorphically:
for obj in [Dog(), Car(), Boat()]:
    obj.move() if hasattr(obj, 'move') else obj.speak()   