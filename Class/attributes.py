# Class vs instance attributes
# class level attributes

class Point:
    default_color = "red"   # Works for instance attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
# Point is class, color will be changed everywhere

point = Point(1, 2)
print(point.default_color)  # instance attribute
print(Point.default_color)  # class level attribute
point.draw()

another = Point(3, 4)
print(another.default_color)    # instance attribute
another.draw()
