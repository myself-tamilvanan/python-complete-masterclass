# Chapter 47: Functional Programming Tips
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 11:20:16
# ============================================

import operator
import functools
import itertools

print("--- Functional Programming Tips ---")

# TIP 1: operator module
print("\n--- Tip 1: operator module ---")
data = [(1, "b"), (3, "a"), (2, "c")]
sorted_data = sorted(data, key=operator.itemgetter(0))
print("Sorted by index 0:", sorted_data)

nums = [3, 1, 4, 1, 5, 9]
total = functools.reduce(operator.add, nums)
product = functools.reduce(operator.mul, [1,2,3,4,5])
print("Sum:", total, "Product:", product)

# TIP 2: Immutability
print("\n--- Tip 2: Immutability ---")
original = [1, 2, 3, 4, 5]
extended = original + [6]
doubled = [x * 2 for x in original]
print("original:", original)
print("extended:", extended)
print("doubled:", doubled)

# TIP 3: Function composition
print("\n--- Tip 3: Composition ---")

def pipe(*fns):
    return functools.reduce(lambda f, g: lambda x: g(f(x)), fns)

clean = pipe(str.strip, str.lower, lambda s: s.replace(" ", "_"))
print("clean:", clean("  Hello World  "))

transform = pipe(lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2)
print("transform(3):", transform(3))

# TIP 4: Memoization
print("\n--- Tip 4: Memoization ---")

@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print("fib(35):", fib(35))
print("Cache info:", fib.cache_info())

# TIP 5: Declarative vs Imperative
print("\n--- Tip 5: Declarative Style ---")

nums = list(range(1, 11))

# Imperative
result_imp = []
for n in nums:
    if n % 2 == 0:
        result_imp.append(n ** 2)

# Declarative (preferred Pythonic style)
result_dec = [n**2 for n in nums if n%2==0]

print("Imperative:", result_imp)
print("Declarative:", result_dec)

# TIP 6: itertools
print("\n--- Tip 6: itertools ---")

first_10_evens = list(itertools.islice(
    filter(lambda x: x%2==0, itertools.count(1)), 10))
print("First 10 evens:", first_10_evens)

data = [("Alice","Eng"),("Bob","Mkt"),("Charlie","Eng"),("Diana","Mkt")]
data_sorted = sorted(data, key=lambda x: x[1])
for dept, members in itertools.groupby(data_sorted, key=lambda x: x[1]):
    print(f"  {dept}: {[m[0] for m in members]}")

print("\n" + "="*50)
print("Chapter 47 Complete!")
print("="*50)