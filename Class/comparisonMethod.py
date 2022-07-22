# Comparing method through magic method

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):    # comparing method
        """
        Without comparing method, point == other result
        will be false.
        __eq__ = equal method
        """
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        # __gt__ = greater than
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point > other)
