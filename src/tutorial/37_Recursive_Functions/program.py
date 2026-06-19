# Chapter 37: Recursive Functions
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:45:31
# ============================================

from functools import lru_cache

print("--- Recursive Functions ---")

# -----------------------------------------------
# SECTION 1: Factorial
# -----------------------------------------------

print("--- Factorial ---")


def factorial(n):
    """n! = n * (n-1)!  Base case: 0! = 1"""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case


for i in range(8):
    print(f"  {i}! = {factorial(i)}")

# -----------------------------------------------
# SECTION 2: Fibonacci
# -----------------------------------------------

print("\n--- Fibonacci ---")


@lru_cache(maxsize=None)
def fibonacci(n):
    """Memoized Fibonacci."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(15)])

# -----------------------------------------------
# SECTION 3: Sum of List
# -----------------------------------------------

print("\n--- Sum of List ---")


def recursive_sum(lst):
    if not lst:
        return 0  # Base case: empty list
    return lst[0] + recursive_sum(lst[1:])


print("Sum:", recursive_sum([1, 2, 3, 4, 5]))  # 15

# -----------------------------------------------
# SECTION 4: Binary Search
# -----------------------------------------------

print("\n--- Binary Search ---")


def binary_search(arr, target, low=0, high=None):
    """Recursively search sorted array."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1  # Base case: not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


data = list(range(0, 20, 2))  # [0, 2, 4, ..., 18]
print("Array:", data)
print("Search 8:", binary_search(data, 8))  # index 4
print("Search 5:", binary_search(data, 5))  # -1 (not found)

# -----------------------------------------------
# SECTION 5: Flatten Nested List
# -----------------------------------------------

print("\n--- Flatten Nested List ---")


def flatten(lst):
    """Recursively flatten a nested list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


nested = [1, [2, 3, [4, 5]], [6, [7, [8, 9]]], 10]
print("Nested:", nested)
print("Flattened:", flatten(nested))

# -----------------------------------------------
# SECTION 6: Tower of Hanoi
# -----------------------------------------------

print("\n--- Tower of Hanoi ---")


def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"  Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"  Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


hanoi(3, "A", "B", "C")

print("\n" + "=" * 50)
print("Chapter 37 Complete!")
print("=" * 50)
