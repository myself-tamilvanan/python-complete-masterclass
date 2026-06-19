# Chapter 20: Operators in Python
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:13:16
# ============================================

# -----------------------------------------------
# SECTION 1: Arithmetic Operators
# -----------------------------------------------

print("--- Arithmetic Operators ---")

a, b = 15, 4
print(f"a={a}, b={b}")
print(f"a + b  = {a + b}")  # 19
print(f"a - b  = {a - b}")  # 11
print(f"a * b  = {a * b}")  # 60
print(f"a / b  = {a / b}")  # 3.75
print(f"a // b = {a // b}")  # 3 (floor)
print(f"a % b  = {a % b}")  # 3 (remainder)
print(f"a ** b = {a**b}")  # 50625

# Practical: Check even/odd
number = 17
print(f"\n{number} is", "even" if number % 2 == 0 else "odd")

# -----------------------------------------------
# SECTION 2: Comparison Operators
# -----------------------------------------------

print("\n--- Comparison Operators ---")

x, y = 10, 20
print(f"x={x}, y={y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >  y: {x > y}")
print(f"x <  y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Chained comparisons (Pythonic!)
age = 25
print(f"\nIs age 18-65? {18 <= age <= 65}")  # True

# -----------------------------------------------
# SECTION 3: Logical Operators
# -----------------------------------------------

print("\n--- Logical Operators ---")

print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)
print("not False:", not False)

# Short-circuit evaluation
print("\nShort-circuit:")
print("0 and print('hi'):", 0 and print("hi"))  # print not called
print("1 or print('hi'):", 1 or print("hi"))  # print not called

# -----------------------------------------------
# SECTION 4: Bitwise Operators
# -----------------------------------------------

print("\n--- Bitwise Operators ---")

a, b = 5, 3  # 5=0b0101, 3=0b0011
print(f"a={a} ({bin(a)}), b={b} ({bin(b)})")
print(f"a & b  = {a & b}  ({bin(a & b)})   # AND")
print(f"a | b  = {a | b}  ({bin(a | b)})   # OR")
print(f"a ^ b  = {a ^ b}  ({bin(a ^ b)})   # XOR")
print(f"~a     = {~a}              # NOT (bitwise complement)")
print(f"a << 1 = {a << 1} ({bin(a << 1)}) # Left shift (multiply by 2)")
print(f"a >> 1 = {a >> 1}  ({bin(a >> 1)}) # Right shift (divide by 2)")


# Practical: check if number is power of 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


for num in [1, 2, 3, 4, 8, 15, 16, 17]:
    print(f"  {num} is power of 2: {is_power_of_two(num)}")

# -----------------------------------------------
# SECTION 5: Assignment Operators
# -----------------------------------------------

print("\n--- Assignment Operators ---")

x = 10
print(f"Initial: x = {x}")

x += 5
print(f"x += 5 → {x}")
x -= 3
print(f"x -= 3 → {x}")
x *= 2
print(f"x *= 2 → {x}")
x //= 3
print(f"x //= 3 → {x}")
x **= 2
print(f"x **= 2 → {x}")
x %= 5
print(f"x %%= 5 → {x}")

# -----------------------------------------------
# SECTION 6: Identity and Membership Operators
# -----------------------------------------------

print("\n--- Identity (is) & Membership (in) ---")

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True (same value)
print(f"a is b: {a is b}")  # False (different objects)
print(f"a is c: {a is c}")  # True (same object)

# Small int caching (Python optimizes -5 to 256)
x = 100
y = 100
print(f"x is y (100): {x is y}")  # True (cached)

# Membership
fruits = ["apple", "banana", "cherry"]
print("\napple in fruits:", "apple" in fruits)  # True
print("mango not in fruits:", "mango" not in fruits)  # True

# in for strings
text = "Hello, World!"
print("World in text:", "World" in text)  # True

# -----------------------------------------------
# SECTION 7: Operator Precedence
# -----------------------------------------------

print("\n--- Operator Precedence ---")

print(2 + 3 * 4)  # 14 (not 20) - * before +
print((2 + 3) * 4)  # 20 - parentheses first
print(2**3**2)  # 512 - ** is right-associative: 2**(3**2)
print(not True or True)  # True - not before or

print("\n" + "=" * 50)
print("Chapter 20 Complete!")
print("=" * 50)
