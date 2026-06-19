# Chapter 51: Itertools
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import operator
from itertools import (
    accumulate,
    chain,
    combinations,
    combinations_with_replacement,
    count,
    cycle,
    groupby,
    islice,
    permutations,
    product,
    repeat,
)

# -----------------------------------------------
# SECTION 1: product - Cartesian Product
# -----------------------------------------------

print("--- product ---")

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # [(1,3),(1,4),(2,3),(2,4)]

# Repeated product (like nested loops)
prod2 = product(a, repeat=2)
print(list(prod2))  # All pairs from a with itself

# -----------------------------------------------
# SECTION 2: permutations
# -----------------------------------------------

print("\n--- permutations ---")

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # All orderings of 3 elements

# Permutations of length r
perm2 = permutations(a, 2)
print(list(perm2))  # All orderings of 2 from 3

# -----------------------------------------------
# SECTION 3: combinations
# -----------------------------------------------

print("\n--- combinations ---")

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # All unique pairs

# With replacement (can repeat elements)
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# -----------------------------------------------
# SECTION 4: accumulate
# -----------------------------------------------

print("\n--- accumulate ---")

a = [1, 2, 3, 4]

# Running sum (default)
acc = accumulate(a)
print("Running sum:", list(acc))  # [1, 3, 6, 10]

# Running product
acc_prod = accumulate(a, func=operator.mul)
print("Running product:", list(acc_prod))  # [1, 2, 6, 24]

# Running max
acc_max = accumulate([3, 1, 4, 1, 5, 9, 2], func=max)
print("Running max:", list(acc_max))

# -----------------------------------------------
# SECTION 5: groupby
# -----------------------------------------------

print("\n--- groupby ---")

# IMPORTANT: Input must be sorted by the grouping key!
persons = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30},
    {"name": "Diana", "age": 30},
    {"name": "Eve", "age": 35},
]

# Sort by age first
persons_sorted = sorted(persons, key=lambda p: p["age"])

for key, group in groupby(persons_sorted, key=lambda p: p["age"]):
    print(f"Age {key}:", [p["name"] for p in group])

# -----------------------------------------------
# SECTION 6: chain and islice
# -----------------------------------------------

print("\n--- chain and islice ---")

# chain - link multiple iterables
combined = chain([1, 2, 3], [4, 5, 6], [7, 8, 9])
print("chain:", list(combined))

# islice - slice an iterator (memory efficient)
gen = (x * x for x in range(1000000))  # Huge generator
first_5 = list(islice(gen, 5))  # Only compute first 5
print("islice first 5 squares:", first_5)

# -----------------------------------------------
# SECTION 7: Infinite Iterators
# -----------------------------------------------

print("\n--- Infinite Iterators ---")

# count - count from start
counter = count(10, 2)  # Start at 10, step 2
print("count:", list(islice(counter, 5)))  # [10, 12, 14, 16, 18]

# cycle - cycle through iterable
cycler = cycle([1, 2, 3])
print("cycle:", list(islice(cycler, 9)))  # [1,2,3,1,2,3,1,2,3]

# repeat - repeat a value
repeater = repeat(42, 4)
print("repeat:", list(repeater))  # [42, 42, 42, 42]

print("\n" + "=" * 50)
print("Chapter 51 Complete!")
print("=" * 50)
