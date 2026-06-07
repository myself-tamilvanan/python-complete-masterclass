# Chapter 19: Type Casting & Type Checking
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:04:35
# ============================================

from typing import Union, Optional, List

# -----------------------------------------------
# SECTION 1: Implicit Type Conversion
# -----------------------------------------------

print("--- Implicit Conversion ---")

# Python automatically converts int to float when needed
x = 10      # int
y = 3.14    # float
result = x + y
print(f"{x} + {y} = {result} (type: {type(result).__name__})")

# int + bool (True=1, False=0)
print(f"10 + True = {10 + True}")    # 11
print(f"10 + False = {10 + False}")  # 10

# -----------------------------------------------
# SECTION 2: Explicit Type Conversion
# -----------------------------------------------

print("\n--- Explicit Type Conversion ---")

# int()
print(int("42"))        # string -> int: 42
print(int(3.99))        # float -> int: 3 (truncates, no rounding)
print(int(True))        # bool -> int: 1
print(int("0b1010", 2)) # binary string -> int: 10
print(int("0xFF", 16))  # hex string -> int: 255

# float()
print(float("3.14"))    # string -> float
print(float(42))        # int -> float: 42.0

# str()
print(str(42))          # int -> string
print(str(3.14))        # float -> string
print(str(True))        # bool -> string: "True"

# bool()
# Falsy values: 0, 0.0, "", [], {}, set(), None, ()
print("\nFalsy values as bool:")
for val in [0, 0.0, "", [], {}, None, ()]:
    print(f"  bool({val!r}) = {bool(val)}")

# Truthy values
print("\nTruthy values as bool:")
for val in [1, -1, "hello", [0], {"a": 1}]:
    print(f"  bool({val!r}) = {bool(val)}")

# Collection conversions
print("\nCollection conversions:")
print("list from string:", list("Python"))
print("tuple from list:", tuple([1, 2, 3]))
print("set from list:", set([1, 2, 2, 3, 3]))
print("list from range:", list(range(5)))

# -----------------------------------------------
# SECTION 3: Safe Type Conversion
# -----------------------------------------------

print("\n--- Safe Type Conversion ---")

def safe_int(value, default=0):
    """Convert to int safely, return default on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))      # 42
print(safe_int("abc"))     # 0 (default)
print(safe_int(None, -1))  # -1 (custom default)

# -----------------------------------------------
# SECTION 4: Type Checking
# -----------------------------------------------

print("\n--- Type Checking ---")

# type() - exact type
values = [42, 3.14, "hello", True, [1,2], (1,2), {1,2}, {"a":1}]
for v in values:
    print(f"  type({v!r}) = {type(v).__name__}")

# isinstance() - preferred for type checking (handles inheritance)
print("\nisinstance() checks:")
print(isinstance(42, int))         # True
print(isinstance(42, float))       # False
print(isinstance(42, (int, float)))# True - check multiple types
print(isinstance(True, int))       # True! bool is subclass of int

# -----------------------------------------------
# SECTION 5: Type Hints (PEP 484)
# -----------------------------------------------

print("\n--- Type Hints ---")

def greet(name: str, times: int = 1) -> str:
    """Greet a person multiple times."""
    return (f"Hello, {name}! " * times).strip()

def process_data(data: List[int]) -> Optional[float]:
    """Return average of list, or None if empty."""
    if not data:
        return None
    return sum(data) / len(data)

def add(a: Union[int, float], b: Union[int, float]) -> float:
    """Add two numbers."""
    return float(a + b)

print(greet("Alice", 2))
print(process_data([1, 2, 3, 4, 5]))
print(add(3, 4.5))

# Type hints do NOT enforce types at runtime
# Use mypy for static checking: pip install mypy

print("\n" + "="*50)
print("Chapter 19 Complete!")
print("="*50)