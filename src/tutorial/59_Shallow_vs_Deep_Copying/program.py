# Chapter 59: Shallow vs Deep Copying
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import copy

# -----------------------------------------------
# SECTION 1: Assignment - NOT a Copy
# -----------------------------------------------

print("--- Assignment (Reference) ---")

# Assignment creates a reference to the SAME object
a = [1, 2, 3, [4, 5]]
b = a  # b points to same list as a

b.append(100)
print("a:", a)  # [1, 2, 3, [4, 5], 100] - BOTH changed!
print("b:", b)
print("Same object?", a is b)  # True

# -----------------------------------------------
# SECTION 2: Shallow Copy
# -----------------------------------------------

print("\n--- Shallow Copy ---")

a = [1, 2, 3, [4, 5]]

# Method 1: copy.copy()
b = copy.copy(a)

# Method 2: list.copy()
c = a.copy()

# Method 3: list slicing
d = a[:]

# Top-level is independent
b.append(100)
print("After b.append(100):")
print("a:", a)  # [1, 2, 3, [4, 5]] - top level unchanged
print("b:", b)  # [1, 2, 3, [4, 5], 100]

# But nested objects are SHARED!
b[3].append(99)
print("\nAfter b[3].append(99):")
print("a:", a)  # [1, 2, 3, [4, 5, 99]] - CHANGED! Shared nested list
print("b:", b)  # [1, 2, 3, [4, 5, 99], 100]

print("Same nested list?", a[3] is b[3])  # True

# -----------------------------------------------
# SECTION 3: Deep Copy
# -----------------------------------------------

print("\n--- Deep Copy ---")

a = [1, 2, 3, [4, 5]]
b = copy.deepcopy(a)

# Top level independent
b.append(100)
print("After b.append(100):")
print("a:", a)  # Unchanged
print("b:", b)

# Nested objects are ALSO independent
b[3].append(99)
print("\nAfter b[3].append(99):")
print("a:", a)  # [1, 2, 3, [4, 5]] - UNCHANGED!
print("b:", b)  # [1, 2, 3, [4, 5, 99], 100]

print("Same nested list?", a[3] is b[3])  # False

# -----------------------------------------------
# SECTION 4: Shallow vs Deep with Objects
# -----------------------------------------------

print("\n--- With Objects ---")


class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __repr__(self):
        return f"Address({self.city}, {self.country})"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"Person({self.name}, {self.address})"


address = Address("New York", "USA")
person1 = Person("Alice", address)

# Shallow copy
person2 = copy.copy(person1)
person2.name = "Bob"  # Does not affect person1
person2.address.city = "Boston"  # Affects person1 (shared)

print("person1:", person1)
print("person2:", person2)

# Reset and deep copy
address = Address("New York", "USA")
person1 = Person("Alice", address)

person3 = copy.deepcopy(person1)
person3.name = "Charlie"
person3.address.city = "Chicago"  # Does NOT affect person1

print("\nAfter deepcopy:")
print("person1:", person1)
print("person3:", person3)

# -----------------------------------------------
# SECTION 5: Dict Copying
# -----------------------------------------------

print("\n--- Dict Copying ---")

original = {"a": 1, "b": [1, 2, 3]}

# Shallow copies
shallow1 = original.copy()
shallow2 = dict(original)

# Deep copy
deep = copy.deepcopy(original)

original["b"].append(99)
print("original:", original)
print("shallow1:", shallow1)  # Also changed!
print("deep:", deep)  # Unchanged

print("\n" + "=" * 50)
print("Chapter 59 Complete!")
print("=" * 50)
