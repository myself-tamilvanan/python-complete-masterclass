# Chapter 28: Instance vs Class vs Static Methods
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:38:27
# ============================================

# -----------------------------------------------
# SECTION 1: Instance Methods
# -----------------------------------------------

print("--- Instance Methods ---")

class Circle:
    pi = 3.14159   # Class variable
    
    def __init__(self, radius):
        self.radius = radius   # Instance variable
    
    # Instance method - accesses self
    def area(self):
        return Circle.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * Circle.pi * self.radius
    
    def scale(self, factor):
        """Modifies instance state."""
        self.radius *= factor

c = Circle(5)
print(f"Area: {c.area():.2f}")
print(f"Circumference: {c.circumference():.2f}")
c.scale(2)
print(f"After scaling radius: {c.radius}")

# -----------------------------------------------
# SECTION 2: Class Methods
# -----------------------------------------------

print("\n--- Class Methods (@classmethod) ---")

class Date:
    """Date class with multiple constructors via classmethods."""
    
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
    
    # Factory method - alternative constructor
    @classmethod
    def from_string(cls, date_str: str):
        """Create Date from string like 2024-01-15."""
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create Date from today's date."""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    @classmethod
    def from_timestamp(cls, timestamp: float):
        """Create Date from Unix timestamp."""
        import datetime
        dt = datetime.datetime.fromtimestamp(timestamp)
        return cls(dt.year, dt.month, dt.day)

# Multiple ways to create a Date object
d1 = Date(2024, 1, 15)
d2 = Date.from_string("2024-06-15")
d3 = Date.today()

print(f"Manual: {d1}")
print(f"From string: {d2}")
print(f"Today: {d3}")

# -----------------------------------------------
# SECTION 3: Static Methods
# -----------------------------------------------

print("\n--- Static Methods (@staticmethod) ---")

class MathHelper:
    """Math utility class - all static methods."""
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if n is a prime number."""
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial of n."""
        if n < 0: raise ValueError("n must be non-negative")
        return 1 if n <= 1 else n * MathHelper.factorial(n - 1)
    
    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return c * 9/5 + 32

# Call without creating an instance
print("Is 17 prime?", MathHelper.is_prime(17))
print("Is 20 prime?", MathHelper.is_prime(20))
print("5! =", MathHelper.factorial(5))
print("100C =", MathHelper.celsius_to_fahrenheit(100), "F")

# -----------------------------------------------
# SECTION 4: Comparison Summary
# -----------------------------------------------

print("\n--- Comparison Summary ---")

class MyClass:
    class_var = "I am a class variable"
    
    def __init__(self, value):
        self.instance_var = value
    
    def instance_method(self):
        return f"Instance: self.instance_var={self.instance_var}, class_var={MyClass.class_var}"
    
    @classmethod
    def class_method(cls):
        return f"Class: class_var={cls.class_var} (no instance access)"
    
    @staticmethod
    def static_method():
        return "Static: no self, no cls - pure utility"

obj = MyClass("hello")
print(obj.instance_method())
print(MyClass.class_method())
print(MyClass.static_method())
print(obj.static_method())  # Can also call on instance

print("\n" + "="*50)
print("Chapter 28 Complete!")
print("="*50)