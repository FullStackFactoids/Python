class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

c = Circle(5)
print(c.radius)  # Output: 5
c.radius = 10
print(c.radius)  # Output: 10

#Fun Facts
class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side * self._side

s = Square(4)
print(s.area)  # Output: 16