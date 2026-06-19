# Chapter 14: Object-Oriented Programming (OOP)
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Basic Class Definition
# -----------------------------------------------

print("--- Basic Class ---")


# class keyword defines a class
class PartyAnimal:
    """A simple class demonstrating OOP basics."""

    # __init__ is the constructor - runs when object is created
    def __init__(self):
        self.x = 0  # Instance attribute

    def party(self):
        """Instance method - self refers to the object."""
        self.x += 1
        print("So far", self.x)


# Create an object (instance) of PartyAnimal
an = PartyAnimal()

# Call methods on the object
an.party()
an.party()
an.party()

# -----------------------------------------------
# SECTION 2: Attributes and Methods
# -----------------------------------------------

print("\n--- Attributes and Methods ---")


class Student:
    """Represents a student with name and grades."""

    def __init__(self, name, student_id):
        """Initialize student with name and ID."""
        self.name = name
        self.student_id = student_id
        self.grades = []  # Empty list for grades

    def add_grade(self, grade):
        """Add a grade to the student record."""
        self.grades.append(grade)

    def get_average(self):
        """Calculate and return average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_info(self):
        """Return a string description of the student."""
        avg = self.get_average()
        return f"Student {self.name} (ID: {self.student_id}), Avg: {avg:.1f}"


# Create student objects
s1 = Student("Alice", "S001")
s2 = Student("Bob", "S002")

# Add grades
s1.add_grade(95)
s1.add_grade(87)
s1.add_grade(92)

s2.add_grade(78)
s2.add_grade(85)

# Display info
print(s1.get_info())
print(s2.get_info())

# -----------------------------------------------
# SECTION 3: Object Lifecycle
# -----------------------------------------------

print("\n--- Object Lifecycle ---")


class LifecycleDemo:
    """Demonstrates __init__ and __del__."""

    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")


obj1 = LifecycleDemo("Object1")
obj2 = LifecycleDemo("Object2")
del obj1  # Manually delete object
print("After deleting obj1")

# -----------------------------------------------
# SECTION 4: Inheritance
# -----------------------------------------------

print("\n--- Inheritance ---")


# Base (parent) class
class Animal:
    """Base class for all animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def __str__(self):
        return f"Animal: {self.name}"


# Child (derived) classes inherit from Animal
class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self):
        # Override parent method
        return f"{self.name} says: Woof!"


class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self):
        return f"{self.name} says: Meow!"


class Bird(Animal):
    """Bird inherits from Animal and adds flying."""

    def speak(self):
        return f"{self.name} says: Tweet!"

    def fly(self):
        return f"{self.name} is flying!"


# Create instances
animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety")]

# Polymorphism - same method name, different behavior
for animal in animals:
    print(animal.speak())

# Check inheritance
dog = Dog("Buddy")
print("\nIs dog an Animal?", isinstance(dog, Animal))  # True
print("Is dog a Dog?", isinstance(dog, Dog))  # True
print("Is dog a Cat?", isinstance(dog, Cat))  # False

# -----------------------------------------------
# SECTION 5: super() - Calling Parent Methods
# -----------------------------------------------

print("\n--- super() ---")


class Person:
    """Person base class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}"


class Employee(Person):
    """Employee extends Person."""

    def __init__(self, name, age, company):
        super().__init__(name, age)  # Call parent constructor
        self.company = company

    def greet(self):
        # Call parent greet and add more info
        base = super().greet()
        return f"{base}, I work at {self.company}"


emp = Employee("Alice", 30, "TechCorp")
print(emp.greet())

print("\n" + "=" * 50)
print("Chapter 14 Complete!")
print("=" * 50)
