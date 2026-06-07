# Chapter 17: Python Architecture & PEP Standards
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamps: 00:55:25 & 01:34:15
# ============================================

import dis    # Disassembler - see bytecode
import sys
import this   # PEP 20: The Zen of Python

# -----------------------------------------------
# SECTION 1: Python Compilation to Bytecode
# -----------------------------------------------

print("--- Python Architecture ---")

# When Python runs your code, it first compiles to bytecode
# You can inspect this with the dis module

def add(a, b):
    """Simple addition function."""
    return a + b

print("Bytecode of add() function:")
dis.dis(add)

# -----------------------------------------------
# SECTION 2: Python Version & Implementation
# -----------------------------------------------

print("\n--- Python Implementation Info ---")
print("Python version:", sys.version)
print("Implementation:", sys.implementation.name)  # cpython, pypy, etc.
print("Platform:", sys.platform)
print("Executable:", sys.executable)

# -----------------------------------------------
# SECTION 3: PEP 20 - The Zen of Python
# -----------------------------------------------

print("\n--- PEP 20: Zen of Python (import this) ---")
# Uncomment to see the Zen:
# import this

# Key principles:
zen_principles = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Readability counts.",
    "Errors should never pass silently.",
    "There should be one obvious way to do it."
]
for p in zen_principles:
    print(" ", p)

# -----------------------------------------------
# SECTION 4: PEP 8 Style Guide Examples
# -----------------------------------------------

print("\n--- PEP 8 Style Examples ---")

# ---- NAMING CONVENTIONS ----

# Variables and functions: snake_case
user_name = "Alice"
total_count = 100

def calculate_area(radius):
    return 3.14159 * radius * radius

# Classes: PascalCase
class BankAccount:
    pass

# Constants: UPPER_CASE
MAX_RETRY_COUNT = 3
PI = 3.14159

# ---- SPACING ----

# Good: spaces around operators
x = 5 + 3
y = x * 2

# Good: no space inside brackets
my_list = [1, 2, 3]
result = my_list[0]

# Good: space after comma
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))

# ---- IMPORTS (correct order per PEP 8) ----
# 1. Standard library imports
# 2. Related third-party imports
# 3. Local application imports

# Good:
import os
import sys
# import numpy as np   # third-party
# from mymodule import myfunction  # local

# ---- DOCSTRINGS (PEP 257) ----

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The BMI value.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    return weight_kg / (height_m ** 2)

print("\nBMI example:", round(calculate_bmi(70, 1.75), 2))

# -----------------------------------------------
# SECTION 5: PEP 572 - Walrus Operator :=
# -----------------------------------------------

print("\n--- PEP 572: Walrus Operator ---")

# Assign and use in same expression (Python 3.8+)
data = [1, 5, 3, 8, 2, 9, 4]

# Without walrus:
n = len(data)
if n > 5:
    print(f"List has {n} elements (> 5)")

# With walrus:
if (n := len(data)) > 5:
    print(f"Walrus: List has {n} elements")

# Useful in while loops:
import io
data_stream = io.StringIO("line1\nline2\nline3\n")
while line := data_stream.readline():
    print("Read:", line.strip())

print("\n" + "="*50)
print("Chapter 17 Complete!")
print("="*50)