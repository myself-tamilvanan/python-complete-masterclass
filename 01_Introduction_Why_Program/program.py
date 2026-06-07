# Chapter 1: Introduction - Why Program?
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Your First Python Program
# -----------------------------------------------

# The print() function outputs text to the screen
print("Hello, World!")
print("Welcome to Python for Everybody!")

# -----------------------------------------------
# SECTION 2: Python as a Calculator
# -----------------------------------------------

print("\n--- Python as a Calculator ---")
print(1 + 1)        # Addition: 2
print(10 - 3)       # Subtraction: 7
print(4 * 5)        # Multiplication: 20
print(10 / 3)       # Division: 3.333...
print(10 // 3)      # Integer division: 3
print(10 % 3)       # Modulo (remainder): 1
print(2 ** 8)       # Exponentiation: 256

# -----------------------------------------------
# SECTION 3: Variables
# -----------------------------------------------

print("\n--- Variables ---")
x = 6           # Assign value 6 to variable x
print(x)        # Output: 6

y = x * 7       # Compute x times 7
print(y)        # Output: 42

# -----------------------------------------------
# SECTION 4: User Input (interactive)
# -----------------------------------------------

print("\n--- User Input Example ---")
# In a real program, uncomment these lines:
# name = input("What is your name? ")
# print("Hello,", name)

# For demonstration:
name = "Dr. Chuck"
print("Hello,", name)

# -----------------------------------------------
# SECTION 5: Error Types
# -----------------------------------------------

print("\n--- Understanding Errors ---")
print("1. Syntax Error - code breaks Python grammar rules")
print("2. Runtime Error - occurs while program runs")
print("3. Semantic Error - code runs but gives wrong output (logic errors)")

print("\n" + "="*50)
print("Chapter 1 Complete!")
print("="*50)