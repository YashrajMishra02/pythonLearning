
# Override speak() method

class Animal:
    def speak(self):
        print("Animal sounds like: ")

class Dog(Animal):
    def speak(self):
        print("Barks")

class Cat(Animal):
    def speak(self):
        print("Meows")

d = Dog()
d.speak()


            # ORRR.......


class Dog(Animal):
    def speak(self):
        super().speak()
        print("brks")
        
d = Dog()
d.speak()