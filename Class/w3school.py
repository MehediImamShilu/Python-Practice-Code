# __init__() representation
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_one = Person("Shilu", 25)

print(person_one.name)
print(person_one.age)

"""

# __str__() representation
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


person_two = Person("Imam", 24)
print(person_two)

"""

# Object method representation


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name + ".")


person_three = Person("Mehedi", 23)
person_three.myfunc()
