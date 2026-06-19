# Chapter 24: OOP - Polymorphism
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 05:57:30
# ============================================

# -----------------------------------------------
# SECTION 1: Method Overriding
# -----------------------------------------------

print("--- Method Overriding ---")


class Shape:
    """Base shape class."""

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def describe(self):
        return (
            f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"
        )


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


# Polymorphic behavior - same interface, different implementation
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

for shape in shapes:
    print(shape.describe())

# -----------------------------------------------
# SECTION 2: Duck Typing
# -----------------------------------------------

print("\n--- Duck Typing ---")


# No common parent needed - just needs the right methods
class Dog:
    def speak(self):
        return "Woof!"

    def move(self):
        return "Dog is running"


class Cat:
    def speak(self):
        return "Meow!"

    def move(self):
        return "Cat is sneaking"


class Robot:
    def speak(self):
        return "Beep boop"

    def move(self):
        return "Robot is rolling"


# This function works with ANY object that has speak() and move()
def make_it_go(creature):
    print(f"  {creature.speak()} | {creature.move()}")


for thing in [Dog(), Cat(), Robot()]:
    make_it_go(thing)

# -----------------------------------------------
# SECTION 3: Operator Overloading
# -----------------------------------------------

print("\n--- Operator Overloading ---")


class Vector:
    """2D vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v2 - v1 = {v2 - v1}")
print(f"v1 * 3 = {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"|v2| = {v2.magnitude():.2f}")

# -----------------------------------------------
# SECTION 4: isinstance() for Polymorphism
# -----------------------------------------------

print("\n--- isinstance() ---")


def process_shape(shape):
    """Process shape with type-specific logic."""
    if isinstance(shape, Circle):
        print(f"  Circle with radius {shape.radius}")
    elif isinstance(shape, Rectangle):
        print(f"  Rectangle {shape.width}x{shape.height}")
    else:
        print(f"  Generic shape: area={shape.area():.2f}")


for s in shapes:
    process_shape(s)

print("\n" + "=" * 50)
print("Chapter 24 Complete!")
print("=" * 50)
