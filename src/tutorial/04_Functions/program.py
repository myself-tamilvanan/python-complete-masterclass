# Chapter 4: Functions
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import math  # Import the math module
import random  # Import the random module

# -----------------------------------------------
# SECTION 1: Built-in Functions
# -----------------------------------------------

print("--- Built-in Functions ---")

# Python comes with many built-in functions
print(len("Hello"))  # 5 - length of string
print(max(3, 1, 4, 1, 5))  # 5 - maximum value
print(min(3, 1, 4, 1, 5))  # 1 - minimum value
print(abs(-42))  # 42 - absolute value
print(round(3.7))  # 4 - round to nearest int
print(round(3.14159, 2))  # 3.14 - round to 2 decimals

# -----------------------------------------------
# SECTION 2: Defining Your Own Functions
# -----------------------------------------------

print("\n--- Defining Functions ---")


# def keyword starts a function definition
def greet():
    """A simple function that prints a greeting."""
    print("Hello! Nice to meet you.")


# Call the function
greet()  # Hello! Nice to meet you.
greet()  # Can call multiple times

# -----------------------------------------------
# SECTION 3: Functions with Parameters
# -----------------------------------------------

print("\n--- Functions with Parameters ---")


def greet_person(name):
    """Greet a specific person by name."""
    print("Hello,", name + "!")


greet_person("Alice")  # Hello, Alice!
greet_person("Bob")  # Hello, Bob!


# Multiple parameters
def add(a, b):
    """Add two numbers and print the result."""
    result = a + b
    print(a, "+", b, "=", result)


add(3, 4)  # 3 + 4 = 7
add(10, 20)  # 10 + 20 = 30

# -----------------------------------------------
# SECTION 4: Return Values
# -----------------------------------------------

print("\n--- Return Values ---")


# Fruitful functions return a value
def square(n):
    """Return the square of a number."""
    return n * n


result = square(5)
print("Square of 5:", result)  # 25

# Can use return value directly
print("Square of 7:", square(7))  # 49


# Function with multiple returns
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)


low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print("Min:", low, "Max:", high)  # Min: 1 Max: 9

# -----------------------------------------------
# SECTION 5: Default Parameters
# -----------------------------------------------

print("\n--- Default Parameters ---")


def power(base, exponent=2):
    """Raise base to the exponent (default 2)."""
    return base**exponent


print(power(3))  # 9 (uses default exponent=2)
print(power(3, 3))  # 27
print(power(2, 10))  # 1024

# -----------------------------------------------
# SECTION 6: Variable Scope
# -----------------------------------------------

print("\n--- Variable Scope ---")

global_var = "I am global"


def show_scope():
    local_var = "I am local"  # Only exists inside function
    print(global_var)  # Can access global variables
    print(local_var)


show_scope()
# print(local_var)  # This would cause NameError!

# -----------------------------------------------
# SECTION 7: Importing Modules
# -----------------------------------------------

print("\n--- Using Modules ---")

# math module
print("Pi:", math.pi)  # 3.14159...
print("Square root of 16:", math.sqrt(16))  # 4.0
print("Ceil of 3.2:", math.ceil(3.2))  # 4
print("Floor of 3.9:", math.floor(3.9))  # 3

# random module
print("\nRandom number (0-1):", random.random())
print("Random int (1-10):", random.randint(1, 10))

print("\n" + "=" * 50)
print("Chapter 4 Complete!")
print("=" * 50)
