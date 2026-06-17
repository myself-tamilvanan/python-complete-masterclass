# Chapter 56: Decorators
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import functools
import time

# -----------------------------------------------
# SECTION 1: First-class Functions
# -----------------------------------------------

print("--- First-class Functions ---")

# Functions can be assigned to variables
def say_hello(name):
    return f"Hello {name}"

greet = say_hello   # Assign without calling
print(greet("Alice"))  # Hello Alice

# Functions can be passed as arguments
def apply(func, value):
    return func(value)

print(apply(str.upper, "hello"))   # HELLO

# Functions can return functions (closures)
def outer(msg):
    def inner():
        print(msg)  # inner remembers msg from outer
    return inner

hi_func = outer("Hi!")
hi_func()   # Hi!

# -----------------------------------------------
# SECTION 2: Basic Decorator
# -----------------------------------------------

print("\n--- Basic Decorator ---")

# A decorator takes a function and returns a modified function
def start_end_decorator(func):
    @functools.wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def print_name(name):
    print(f"Name: {name}")

print_name("Alex")

# -----------------------------------------------
# SECTION 3: Practical Decorators
# -----------------------------------------------

print("\n--- Timing Decorator ---")

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "done"

result = slow_function()
print("Result:", result)

# Debugging decorator
def debug_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug_decorator
def add(a, b):
    return a + b

add(3, 4)

# -----------------------------------------------
# SECTION 4: Decorator with Arguments
# -----------------------------------------------

print("\n--- Decorator with Arguments ---")

# Need an extra layer of nesting
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()   # Prints "Hi!" 3 times

# -----------------------------------------------
# SECTION 5: Stacking Decorators
# -----------------------------------------------

print("\n--- Stacking Decorators ---")

# Multiple decorators applied bottom-up
@debug_decorator
@timer_decorator
def compute(x, y):
    time.sleep(0.05)
    return x**2 + y**2

compute(3, 4)

# -----------------------------------------------
# SECTION 6: Class-based Decorators
# -----------------------------------------------

print("\n--- Class-based Decorator ---")

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call #{self.num_calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
print(f"greet was called {greet.num_calls} times")

print("\n" + "="*50)
print("Chapter 56 Complete!")
print("="*50)
