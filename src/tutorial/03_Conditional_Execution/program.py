# Chapter 3: Conditional Execution
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Basic if Statement
# -----------------------------------------------

print("--- Basic if Statement ---")

x = 5

# Code inside if block only runs when condition is True
if x > 0:
    print("x is positive")  # Runs because 5 > 0 is True

if x < 0:
    print("x is negative")  # Does NOT run because 5 < 0 is False

# -----------------------------------------------
# SECTION 2: if/else
# -----------------------------------------------

print("\n--- if/else ---")

temperature = 35

if temperature > 30:
    print("It is hot outside!")
else:
    print("It is not that hot.")

# -----------------------------------------------
# SECTION 3: if/elif/else
# -----------------------------------------------

print("\n--- if/elif/else ---")

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Score:", score, "Grade:", grade)

# -----------------------------------------------
# SECTION 4: Comparison Operators
# -----------------------------------------------

print("\n--- Comparison Operators ---")

a, b = 10, 20
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a <  b:", a < b)  # True
print("a >  b:", a > b)  # False
print("a <= b:", a <= b)  # True
print("a >= b:", a >= b)  # False

# -----------------------------------------------
# SECTION 5: Logical Operators
# -----------------------------------------------

print("\n--- Logical Operators ---")

age = 25
has_license = True

# and: BOTH must be True
if age >= 18 and has_license:
    print("You can drive!")

# or: at least ONE must be True
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No school today!")

# not: reverses the boolean
is_raining = False
if not is_raining:
    print("Good day for a walk!")

# -----------------------------------------------
# SECTION 6: try/except Error Handling
# -----------------------------------------------

print("\n--- try/except ---")

# Without try/except bad input crashes program
# With try/except we handle it gracefully

user_input = "abc"
try:
    value = int(user_input)
    print("Converted:", value)
except ValueError:
    print("Cannot convert", user_input, "to integer")

user_input2 = "42"
try:
    value2 = int(user_input2)
    print("Converted:", value2)
except ValueError:
    print("Cannot convert", user_input2, "to integer")

# -----------------------------------------------
# SECTION 7: Guardian Pattern
# -----------------------------------------------

print("\n--- Guardian Pattern ---")


def safe_divide(a, b):
    # Guard against division by zero
    if b == 0:
        print("Cannot divide by zero!")
        return None
    return a / b


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Error message

print("\n" + "=" * 50)
print("Chapter 3 Complete!")
print("=" * 50)
