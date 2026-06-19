# Chapter 31: Pure vs Impure Functions
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:10:34
# ============================================

# -----------------------------------------------
# SECTION 1: Pure Functions
# -----------------------------------------------

print("--- Pure Functions ---")


# Pure: same input ALWAYS gives same output, no side effects
def add(a, b):
    return a + b


def square(x):
    return x * x


def get_full_name(first, last):
    return f"{first} {last}"


print(add(2, 3))  # Always 5
print(add(2, 3))  # Always 5
print(square(4))  # Always 16
print(get_full_name("Alice", "Smith"))

# -----------------------------------------------
# SECTION 2: Impure Functions
# -----------------------------------------------

print("\n--- Impure Functions ---")

count = 0


# Impure: modifies global state
def increment():
    global count
    count += 1
    return count


print(increment())  # 1
print(increment())  # 2 - different result with same (no) input!
print(increment())  # 3

import random


# Impure: result depends on external state
def random_greet(name):
    greetings = ["Hello", "Hi", "Hey"]
    return random.choice(greetings) + ", " + name


print(random_greet("Alice"))  # Unpredictable
print(random_greet("Alice"))  # Different each time


# Impure: mutates input
def add_to_list_bad(item, lst):
    lst.append(item)  # Modifies the original list!
    return lst


my_list = [1, 2, 3]
add_to_list_bad(4, my_list)
print("List after call:", my_list)  # [1, 2, 3, 4] - modified!

# -----------------------------------------------
# SECTION 3: Refactoring Impure to Pure
# -----------------------------------------------

print("\n--- Refactoring to Pure ---")


# IMPURE: mutates list
def add_to_list_bad(item, lst):
    lst.append(item)
    return lst


# PURE: returns new list
def add_to_list_pure(item, lst):
    return lst + [item]  # Creates NEW list


original = [1, 2, 3]
result = add_to_list_pure(4, original)
print("Original:", original)  # [1, 2, 3] - unchanged!
print("Result:", result)  # [1, 2, 3, 4]

# IMPURE: reads external state
import datetime


def get_greeting_impure():
    hour = datetime.datetime.now().hour
    return "Good morning" if hour < 12 else "Good evening"


# PURE: time is passed as argument
def get_greeting_pure(hour):
    return "Good morning" if hour < 12 else "Good evening"


print(get_greeting_pure(9))
print(get_greeting_pure(18))

# -----------------------------------------------
# SECTION 4: Memoization (caching pure functions)
# -----------------------------------------------

print("\n--- Memoization (only safe for pure functions) ---")

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """Pure + memoized Fibonacci."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


import time

start = time.time()
print("fib(35):", fibonacci(35))
print(f"Time: {time.time() - start:.4f}s")

# Second call is instant (cached)
start = time.time()
print("fib(35) again:", fibonacci(35))
print(f"Cached time: {time.time() - start:.6f}s")

print("\n" + "=" * 50)
print("Chapter 31 Complete!")
print("=" * 50)
