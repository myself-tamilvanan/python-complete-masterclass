# Chapter 49: Sets
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

# -----------------------------------------------
# SECTION 1: Creating Sets
# -----------------------------------------------

print("--- Sets ---")

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Sets remove duplicates automatically
my_set2 = {1, 2, 2, 3, 3, 3}
print(my_set2)  # {1, 2, 3}

# Create from list (deduplicate)
my_list = [1, 2, 2, 3, 4, 4, 5]
unique = set(my_list)
print("Unique:", unique)

# Empty set - must use set() not {}
empty = set()  # {} would create empty dict!
print("Empty set type:", type(empty))

# -----------------------------------------------
# SECTION 2: Set Methods
# -----------------------------------------------

print("\n--- Set Methods ---")

my_set = {1, 2, 3}

# add
my_set.add(4)
print("add 4:", my_set)

# remove - raises KeyError if not found
my_set.remove(3)
print("remove 3:", my_set)

# discard - no error if not found
my_set.discard(99)  # No error
print("discard 99:", my_set)

# pop - remove random element
popped = my_set.pop()
print("popped:", popped)

# -----------------------------------------------
# SECTION 3: Set Operations
# -----------------------------------------------

print("\n--- Set Operations ---")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union - all elements from both
print("Union (|):", a | b)
print("Union method:", a.union(b))

# Intersection - elements in both
print("Intersection (&):", a & b)
print("Intersection method:", a.intersection(b))

# Difference - in a but not b
print("Difference (-):", a - b)
print("Difference method:", a.difference(b))

# Symmetric difference - in either but not both
print("Symmetric diff (^):", a ^ b)
print("Symmetric method:", a.symmetric_difference(b))

# -----------------------------------------------
# SECTION 4: Set Relationships
# -----------------------------------------------

print("\n--- Set Relationships ---")

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print("a subset of b:", a.issubset(b))  # True
print("b superset of a:", b.issuperset(a))  # True
print("Disjoint:", a.isdisjoint({6, 7}))  # True (no common)

# -----------------------------------------------
# SECTION 5: Set Comprehensions
# -----------------------------------------------

print("\n--- Set Comprehensions ---")

# Like list comprehensions but with {}
squares = {x * x for x in range(-5, 6)}
print("Squares set:", sorted(squares))

# -----------------------------------------------
# SECTION 6: Frozen Sets
# -----------------------------------------------

print("\n--- Frozen Sets ---")

# frozenset is immutable - can be used as dict key
fs = frozenset([1, 2, 3])
print("frozenset:", fs)

# Use as dict key
my_dict = {frozenset([1, 2]): "pair", frozenset([3, 4, 5]): "triple"}
print(my_dict[frozenset([1, 2])])

# -----------------------------------------------
# SECTION 7: Performance - Membership Test
# -----------------------------------------------

print("\n--- Performance ---")

import timeit

large_list = list(range(100000))
large_set = set(range(100000))

list_time = timeit.timeit("99999 in large_list", globals=globals(), number=1000)
set_time = timeit.timeit("99999 in large_set", globals=globals(), number=1000)

print(f"List membership: {list_time:.4f}s")
print(f"Set membership:  {set_time:.6f}s")
print(f"Set is ~{list_time / set_time:.0f}x faster")

print("\n" + "=" * 50)
print("Chapter 49 Complete!")
print("=" * 50)
