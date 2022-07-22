# Exapmle of method overriding
# same code from inheritance

class Animal:
    def __init__(self):
        print("Animal Constractor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        # method overriding
        # super().__init__()
        # output will be Animal first then Mammal
        print("Mammal Constractor")
        self.weight = 2
        # method overriding
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
