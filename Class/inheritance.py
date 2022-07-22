# NOTE: Simple example of inheritance
# Where Mammal & Fish; both are Animal

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base class
# Mammal: Child, Sub-class
class Mammal(Animal):
    def walk(self):
        print("walk")


# Animal: Parent, Base class
# Fish: Child, Sub-class
class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
# checking default object class
print(isinstance(m, Animal))
print(issubclass(Mammal, Animal))
