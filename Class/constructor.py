# Create a constructor

class Point:
    def __init__(self, x, y):   # Here, __init__ is a constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
