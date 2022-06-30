# This is my first class
# From: Mosh's Python Tutorial

class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))  # type: <class '__main__.Point'>
print(isinstance(point, Point))     # True
