# Here is two different code to show multiple inheritance

class Employee:
    def greet(self):
        print("Greet Employee")


class Person:
    def greet(self):
        print("Greet Person")


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()

# Here is a good example of multi level inheritance
"""
class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
"""
