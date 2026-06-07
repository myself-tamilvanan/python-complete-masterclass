# Chapter 32: Lambda, Map, Filter, Reduce
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:15:34
# ============================================

from functools import reduce
import operator

# -----------------------------------------------
# SECTION 1: Lambda Functions
# -----------------------------------------------

print("--- Lambda Functions ---")

# Simple lambdas
square = lambda x: x ** 2
add = lambda x, y: x + y
greet = lambda name: f"Hello, {name}!"
is_even = lambda n: n % 2 == 0

print(square(5))        # 25
print(add(3, 4))         # 7
print(greet("Gowtham")) # Hello, Gowtham!
print(is_even(6))        # True

# Lambda in sorted
students = [{"name": "Charlie", "gpa": 3.2}, {"name": "Alice", "gpa": 3.8}, {"name": "Bob", "gpa": 3.5}]
sorted_students = sorted(students, key=lambda s: s["gpa"], reverse=True)
for s in sorted_students:
    print(f"  {s['name']}: {s['gpa']}")

# -----------------------------------------------
# SECTION 2: map()
# -----------------------------------------------

print("\n--- map() ---")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)

# Convert temperatures
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print("Fahrenheit:", fahrenheit)

# -----------------------------------------------
# SECTION 3: filter()
# -----------------------------------------------

print("\n--- filter() ---")

primes_check = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
primes = list(filter(primes_check, range(2, 50)))
print("Primes < 50:", primes)

words = ["apple", "banana", "cherry", "avocado", "blueberry"]
a_words = list(filter(lambda w: w.startswith("a"), words))
print("Words starting with a:", a_words)

# -----------------------------------------------
# SECTION 4: reduce()
# -----------------------------------------------

print("\n--- reduce() ---")

nums = [1, 2, 3, 4, 5]
print("Sum:", reduce(operator.add, nums))        # 15
print("Product:", reduce(operator.mul, nums))    # 120
print("Max:", reduce(lambda x, y: x if x > y else y, nums))  # 5

# With initial value
print("Sum + 100:", reduce(operator.add, nums, 100))  # 115

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda a, b: a + b, words)
print("Sentence:", sentence)

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda a, b: a + b, nested)
print("Flattened:", flat)

# -----------------------------------------------
# SECTION 5: Combining All Three
# -----------------------------------------------

print("\n--- Combined Pipeline ---")

data = list(range(1, 21))

# Find sum of squares of even numbers
result = reduce(
    operator.add,
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, data))
)

print("Sum of squares of even 1-20:", result)

# Equivalent with comprehension
result2 = sum(x**2 for x in data if x % 2 == 0)
print("List comprehension result:", result2)

print("\n" + "="*50)
print("Chapter 32 Complete!")
print("="*50)