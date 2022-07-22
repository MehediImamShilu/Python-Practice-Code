# magic method: __...__

class Point:
    def __init__(self, x, y):
        # __init__ is magic method
        self.x = x
        self.y = y

    def __str__(self):
        # __str__ is magic method
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(str(point))
