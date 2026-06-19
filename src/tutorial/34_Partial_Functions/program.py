# Chapter 34: Partial Functions
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:34:53
# ============================================

from functools import partial

print("--- Partial Functions ---")


# Original function
def power(base, exponent):
    return base**exponent


# Create specialized versions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("square(4):", square(4))  # 16
print("cube(3):", cube(3))  # 27

# Using partial with map
numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print("Squares:", squares)


# Partial with multiple pre-filled args
def greet(greeting, name, punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


say_hello = partial(greet, "Hello")
say_hi_formal = partial(greet, "Hello", punctuation=".")

print(say_hello("Alice"))
print(say_hello("Bob", punctuation="?"))
print(say_hi_formal("Dr. Smith"))


# Practical: URL builder
def build_url(protocol, domain, path="/"):
    return f"{protocol}://{domain}{path}"


https_url = partial(build_url, "https")
api_url = partial(build_url, "https", "api.example.com")

print(https_url("example.com"))
print(https_url("example.com", "/about"))
print(api_url("/users"))
print(api_url("/products/42"))

print("\n" + "=" * 50)
print("Chapter 34 Complete!")
print("=" * 50)
