# Python crush course

class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Intialize name & age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting on command"""
        print(self.name.title() + " is sitting on a wall.")

    def roll_over(self):
        """Rolling over on a command"""
        print(self.name.title() + " is rolling on the age of " + str(self.age) + ".")


my_dog = Dog("jake", 6)
your_dog = Dog("piyash", 4)

print("The name of my dog is " + my_dog.name.title() + ".")
print(my_dog.name.title() + " is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("\nThe name of my dog is " + your_dog.name.title() + ".")
print(your_dog.name.title() + " is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
