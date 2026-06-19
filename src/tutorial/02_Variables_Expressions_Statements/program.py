# Chapter 2: Variables, Expressions, and Statements
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Variables and Assignment
# -----------------------------------------------

print("--- Variables and Assignment ---")

# Variables store data; use = for assignment
x = 12.2  # float variable
y = 14  # integer variable

print(x)  # 12.2
print(y)  # 14

# Variables can be reassigned
x = 100
print(x)  # 100

# -----------------------------------------------
# SECTION 2: Data Types
# -----------------------------------------------

print("\n--- Data Types ---")

integer_val = 42
float_val = 3.14
string_val = "Hello"
bool_val = True

# type() shows what type a value is
print(type(integer_val))  # <class "int">
print(type(float_val))  # <class "float">
print(type(string_val))  # <class "str">
print(type(bool_val))  # <class "bool">

# -----------------------------------------------
# SECTION 3: Type Conversion
# -----------------------------------------------

print("\n--- Type Conversion ---")

# int() converts to integer
print(int("42"))  # string to int: 42
print(int(3.99))  # float to int: 3 (truncates)

# float() converts to float
print(float("3.14"))  # string to float: 3.14
print(float(42))  # int to float: 42.0

# str() converts to string
print(str(42))  # int to string: "42"

# -----------------------------------------------
# SECTION 4: Arithmetic Operators
# -----------------------------------------------

print("\n--- Arithmetic Operators ---")

a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b)  # 3  (floor division)
print(a % b)  # 1  (remainder)
print(a**b)  # 1000 (10 to the power of 3)

# -----------------------------------------------
# SECTION 5: Order of Operations
# -----------------------------------------------

print("\n--- Order of Operations (PEMDAS) ---")

result1 = 2 + 3 * 4  # Multiplication first: 14
result2 = (2 + 3) * 4  # Parentheses first: 20
result3 = 2**3 + 1  # Exponent first: 9

print(result1)  # 14
print(result2)  # 20
print(result3)  # 9

# -----------------------------------------------
# SECTION 6: String Operations
# -----------------------------------------------

print("\n--- String Operations ---")

first = "Hello"
second = "World"

# Concatenation
combined = first + " " + second
print(combined)  # Hello World

# Repetition
repeated = "Ha" * 3
print(repeated)  # HaHaHa

# String length
print(len(combined))  # 11

# -----------------------------------------------
# SECTION 7: User Input
# -----------------------------------------------

print("\n--- User Input ---")

# input() always returns a string
# Uncomment to use interactively:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))  # Convert to int

# Demonstration:
age = int("25")  # Simulated input converted to int
print("Next year you will be:", age + 1)

print("\n" + "=" * 50)
print("Chapter 2 Complete!")
print("=" * 50)
