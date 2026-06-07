# Chapter 8: Python Lists
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Creating Lists
# -----------------------------------------------

print("--- Creating Lists ---")

# Lists are created with square brackets
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]   # Lists can hold different types
empty = []                          # Empty list

print(numbers)
print(fruits)
print(mixed)

# -----------------------------------------------
# SECTION 2: Indexing and Slicing
# -----------------------------------------------

print("\n--- Indexing and Slicing ---")

colors = ["red", "green", "blue", "yellow", "purple"]

print(colors[0])       # red (first item)
print(colors[-1])      # purple (last item)
print(colors[1:3])     # ["green", "blue"]
print(colors[:3])      # first 3 items
print(colors[2:])      # from index 2 to end

# Lists are MUTABLE - can change items
colors[0] = "orange"
print(colors)          # orange is now first

# -----------------------------------------------
# SECTION 3: List Methods
# -----------------------------------------------

print("\n--- List Methods ---")

items = [3, 1, 4, 1, 5, 9, 2, 6]

# append() - add to end
items.append(10)
print("After append:", items)

# insert() - add at specific position
items.insert(0, 0)    # Insert 0 at index 0
print("After insert:", items)

# pop() - remove and return last item
removed = items.pop()
print("Popped:", removed)
print("After pop:", items)

# remove() - remove by value
items.remove(1)       # Removes FIRST occurrence of 1
print("After remove:", items)

# sort() - sort in place
items.sort()
print("Sorted:", items)

# reverse() - reverse in place
items.reverse()
print("Reversed:", items)

# -----------------------------------------------
# SECTION 4: List Operations and Functions
# -----------------------------------------------

print("\n--- List Operations ---")

nums = [3, 1, 4, 1, 5, 9]

print("Length:", len(nums))     # 6
print("Sum:", sum(nums))         # 23
print("Max:", max(nums))         # 9
print("Min:", min(nums))         # 1

# in operator
print("5 in nums:", 5 in nums)   # True
print("7 in nums:", 7 in nums)   # False

# count occurrences
print("Count of 1:", nums.count(1))  # 2

# -----------------------------------------------
# SECTION 5: Strings vs. Lists
# -----------------------------------------------

print("\n--- Strings vs. Lists ---")

# Strings are immutable, lists are mutable
word = "Python"
# word[0] = "J"  # This would cause TypeError!

# Convert string to list of characters
chars = list("Python")
print(chars)      # ["P", "y", "t", "h", "o", "n"]

# split() converts string to list
sentence = "Hello World Python"
words = sentence.split()
print(words)      # ["Hello", "World", "Python"]

# join() converts list to string
rejoined = " ".join(words)
print(rejoined)   # Hello World Python

# -----------------------------------------------
# SECTION 6: Loop Patterns with Lists
# -----------------------------------------------

print("\n--- Loop Patterns ---")

scores = [85, 92, 78, 96, 88, 73, 90]

# Build a list of passing scores
passing = []
for score in scores:
    if score >= 80:
        passing.append(score)
print("Passing scores:", passing)

# List comprehension (Pythonic way)
passing2 = [s for s in scores if s >= 80]
print("Passing (comprehension):", passing2)

# -----------------------------------------------
# SECTION 7: Guardian Pattern
# -----------------------------------------------

print("\n--- Guardian Pattern ---")

email_data = ["From alice@example.com", "Subject: Hello",
              "From bob@example.com", "Date: Jan 5",
              "From charlie@example.com"]

senders = []
for line in email_data:
    # Guard: only process "From" lines
    if not line.startswith("From "):
        continue
    parts = line.split()
    if len(parts) >= 2:   # Guard: ensure we have enough parts
        senders.append(parts[1])

print("Senders:", senders)

print("\n" + "="*50)
print("Chapter 8 Complete!")
print("="*50)