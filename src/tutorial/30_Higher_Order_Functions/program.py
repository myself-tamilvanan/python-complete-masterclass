# Chapter 30: Higher Order Functions
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 07:53:00
# ============================================

from functools import reduce

# -----------------------------------------------
# SECTION 1: Functions as Arguments
# -----------------------------------------------

print("--- Functions as Arguments ---")


def apply_twice(func, value):
    """Apply a function twice to a value."""
    return func(func(value))


def double(x):
    return x * 2


def square(x):
    return x * x


print(apply_twice(double, 3))  # 12 (3 -> 6 -> 12)
print(apply_twice(square, 2))  # 16 (2 -> 4 -> 16)

# -----------------------------------------------
# SECTION 2: map()
# -----------------------------------------------

print("\n--- map() ---")

numbers = [1, 2, 3, 4, 5]

# Apply function to each element
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

names = ["alice", "bob", "charlie"]
capitalized = list(map(str.capitalize, names))
print("Capitalized:", capitalized)

# Map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print("Sums:", sums)

# -----------------------------------------------
# SECTION 3: filter()
# -----------------------------------------------

print("\n--- filter() ---")

data = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

positives = list(filter(lambda x: x > 0, data))
print("Positives:", positives)

evens = list(filter(lambda x: x % 2 == 0, data))
print("Evens:", evens)

# -----------------------------------------------
# SECTION 4: reduce()
# -----------------------------------------------

print("\n--- reduce() ---")

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
product = reduce(lambda x, y: x * y, nums)
maximum = reduce(lambda x, y: x if x > y else y, nums)

print("Sum:", total)
print("Product:", product)
print("Max:", maximum)

# -----------------------------------------------
# SECTION 5: Functions Returning Functions
# -----------------------------------------------

print("\n--- Functions Returning Functions ---")


def make_multiplier(factor):
    """Returns a function that multiplies by factor."""

    def multiplier(x):
        return x * factor

    return multiplier


triple = make_multiplier(3)
print("Triple 5:", triple(5))  # 15

tenx = make_multiplier(10)
print("10x 7:", tenx(7))  # 70


# Practical: Create grader function
def make_grader(thresholds):
    """Returns a grading function for given thresholds."""

    def grade(score):
        for threshold, letter in sorted(thresholds.items(), reverse=True):
            if score >= threshold:
                return letter
        return "F"

    return grade


standard_grade = make_grader({90: "A", 80: "B", 70: "C", 60: "D"})
print("Score 85:", standard_grade(85))
print("Score 72:", standard_grade(72))
print("Score 55:", standard_grade(55))

# -----------------------------------------------
# SECTION 6: Custom Higher-Order Functions
# -----------------------------------------------

print("\n--- Custom HOFs ---")


def transform_data(data, *funcs):
    """Apply a series of functions to data."""
    result = data
    for func in funcs:
        result = list(map(func, result))
    return result


numbers = [1, 2, 3, 4, 5]
result = transform_data(numbers, lambda x: x * 2, lambda x: x + 10, str)
print("Transformed:", result)

print("\n" + "=" * 50)
print("Chapter 30 Complete!")
print("=" * 50)
