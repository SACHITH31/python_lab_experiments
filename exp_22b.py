import math

# Base class
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

# Circle
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r * self.r
    
    def perimeter(self):
        return 2 * math.pi * self.r

# Square
class Square(Shape):
    def __init__(self, s):
        self.s = s
    
    def area(self):
        return self.s * self.s
    
    def perimeter(self):
        return 4 * self.s

# Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Testing
c = Circle(5)
s = Square(4)
t = Triangle(3, 4, 5)

print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())

print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())

# output:
# Circle Area: 78.53981633974483
# Circle Perimeter: 31.41592653589793
# Square Area: 16
# Square Perimeter: 16
# Triangle Area: 6.0
# Triangle Perimeter: 12
