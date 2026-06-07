# Chapter 23: OOP - Constructors in Python
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 05:19:47
# ============================================

# -----------------------------------------------
# SECTION 1: Default Constructor
# -----------------------------------------------

print("--- Default Constructor ---")

class Dog:
    """A dog class with a default constructor."""
    
    def __init__(self):
        """Default constructor - no parameters."""
        self.sound = "Woof"
        self.legs = 4
    
    def speak(self):
        return self.sound

dog = Dog()
print("Sound:", dog.speak())
print("Legs:", dog.legs)

# -----------------------------------------------
# SECTION 2: Parameterized Constructor
# -----------------------------------------------

print("\n--- Parameterized Constructor ---")

class Student:
    """A student class with parameterized constructor."""
    
    # Class variable (shared by all instances)
    school_name = "Python Academy"
    student_count = 0
    
    def __init__(self, name: str, age: int, grade: str = "A"):
        """Initialize student with name, age, and optional grade."""
        self.name = name        # Instance variable
        self.age = age
        self.grade = grade
        Student.student_count += 1   # Update class variable
    
    def __str__(self):
        """String representation of the student."""
        return f"Student({self.name}, age={self.age}, grade={self.grade})"
    
    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age}, grade={self.grade!r})"

s1 = Student("Alice", 20)
s2 = Student("Bob", 22, "B+")
s3 = Student("Charlie", 19, "A+")

print(s1)
print(s2)
print(f"Total students: {Student.student_count}")
print(f"School: {Student.school_name}")

# -----------------------------------------------
# SECTION 3: super().__init__() in Inheritance
# -----------------------------------------------

print("\n--- super() in Constructor ---")

class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound
        print(f"  Animal __init__: {name}")
    
    def speak(self):
        return f"{self.name} says {self.sound}"

class Cat(Animal):
    def __init__(self, name: str, indoor: bool = True):
        super().__init__(name, "Meow")  # Call parent constructor
        self.indoor = indoor
        print(f"  Cat __init__: {name}, indoor={indoor}")

class PoliceDog(Animal):
    def __init__(self, name: str, badge_number: str):
        super().__init__(name, "Woof")
        self.badge_number = badge_number
    
    def __str__(self):
        return f"PoliceDog({self.name}, badge={self.badge_number})"

cat = Cat("Whiskers")
print(cat.speak())

police_dog = PoliceDog("Rex", "K9-007")
print(police_dog)

# -----------------------------------------------
# SECTION 4: __new__ vs __init__
# -----------------------------------------------

print("\n--- __new__ vs __init__ ---")

class Singleton:
    """Example of Singleton pattern using __new__."""
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        """Create only one instance."""
        if cls._instance is None:
            print("  Creating new Singleton instance")
            cls._instance = super().__new__(cls)
        else:
            print("  Returning existing instance")
        return cls._instance
    
    def __init__(self, value):
        self.value = value

s1 = Singleton(10)
s2 = Singleton(20)
s3 = Singleton(30)

print(f"s1 is s2: {s1 is s2}")  # True - same object
print(f"s3.value: {s3.value}")  # 30 - __init__ called each time

# -----------------------------------------------
# SECTION 5: Destructor __del__
# -----------------------------------------------

print("\n--- Destructor __del__ ---")

class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        print(f"  Connection opened to {host}")
    
    def __del__(self):
        print(f"  Connection closed to {self.host}")

conn = DatabaseConnection("localhost")
print("  Using connection...")
del conn   # Calls __del__

print("\n" + "="*50)
print("Chapter 23 Complete!")
print("="*50)