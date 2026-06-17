# Chapter 58: The Asterisk (*) Operator
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

# -----------------------------------------------
# SECTION 1: Basic Uses
# -----------------------------------------------

print("--- Basic Uses ---")

# Multiplication
print("5 * 3 =", 5 * 3)

# Power
print("2 ** 8 =", 2 ** 8)

# String repetition
print("Ha" * 3)  # HaHaHa

# List repetition
print([0] * 5)   # [0, 0, 0, 0, 0]

# -----------------------------------------------
# SECTION 2: Unpacking Iterables
# -----------------------------------------------

print("\n--- Unpacking Iterables ---")

# Unpack list into function args
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print("Unpack list:", add(*numbers))  # Same as add(1, 2, 3)

# Unpack in print
fruits = ["apple", "banana", "cherry"]
print(*fruits)            # apple banana cherry
print(*fruits, sep=", ")  # apple, banana, cherry

# Combine iterables with *
a = [1, 2, 3]
b = [4, 5, 6]
combined = [*a, *b]
print("Combined:", combined)

# Unpack string characters
chars = [*"Python"]
print("Characters:", chars)

# -----------------------------------------------
# SECTION 3: Unpacking Dicts
# -----------------------------------------------

print("\n--- Unpacking Dicts ---")

# Unpack dict as keyword args
def introduce(name, age, city):
    print(f"I am {name}, {age} from {city}")

person = {"name": "Alice", "age": 30, "city": "NYC"}
introduce(**person)

# Merge dicts with **
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"b": 99, "e": 5}  # Overlapping key

merged = {**d1, **d2}
print("Merged:", merged)

# Later dict overwrites earlier (b=99 from d3)
merged2 = {**d1, **d3}
print("With override:", merged2)

# -----------------------------------------------
# SECTION 4: Extended Unpacking in Assignments
# -----------------------------------------------

print("\n--- Extended Unpacking ---")

first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")

*beginning, last = [1, 2, 3, 4, 5]
print(f"beginning={beginning}, last={last}")

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# Useful for ignoring parts
a, *_, z = [1, 2, 3, 4, 5]
print(f"a={a}, z={z} (middle ignored)")

# -----------------------------------------------
# SECTION 5: Keyword-only Arguments
# -----------------------------------------------

print("\n--- Keyword-only Args ---")

# Everything after bare * must be keyword
def func(a, b, *, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")

func(1, 2, c=3, d=4)         # OK
# func(1, 2, 3, 4)           # TypeError!

# Combine with *args
def func2(a, *args, keyword_only):
    print(f"a={a}, args={args}, kw={keyword_only}")

func2(1, 2, 3, 4, keyword_only="must use keyword")

# -----------------------------------------------
# SECTION 6: Practical Patterns
# -----------------------------------------------

print("\n--- Practical Patterns ---")

# Flexible function accepting any args
def log(message, *args, level="INFO", **kwargs):
    print(f"[{level}] {message}")
    if args:
        print(f"  Extra args: {args}")
    if kwargs:
        print(f"  Extra info: {kwargs}")

log("System started")
log("User login", "extra1", level="DEBUG", user="alice", ip="127.0.0.1")

print("\n" + "="*50)
print("Chapter 58 Complete!")
print("="*50)
