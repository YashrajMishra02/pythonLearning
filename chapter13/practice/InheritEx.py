
# Create Animal → Dog, Cat, Bird hierarchy using inheritance + polymorphism. Override speak() and move().

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating ")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

class Bird(Animal):
    def koo(self):
        print(f"{self.name} says: kouoo")

d = Dog("bhola")
d.bark()
d.eat()

c = Cat("twinkle")
c.meow()
c.sleep()

b = Bird("darud")
b.koo()
b.eat()
b.sleep()
