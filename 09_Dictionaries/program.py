# Chapter 9: Dictionaries
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Creating Dictionaries
# -----------------------------------------------

print("--- Creating Dictionaries ---")

# Dictionary: key-value pairs in curly braces
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person)
print(person["name"])   # Alice
print(person["age"])    # 30

# Empty dictionary
empty = {}
print("Empty dict:", empty)

# -----------------------------------------------
# SECTION 2: Adding and Modifying
# -----------------------------------------------

print("\n--- Adding and Modifying ---")

scores = {}

# Add new key-value pairs
scores["Alice"] = 95
scores["Bob"] = 87
scores["Charlie"] = 92
print("Scores:", scores)

# Modify existing value
scores["Alice"] = 98
print("Updated scores:", scores)

# -----------------------------------------------
# SECTION 3: Checking Keys Safely
# -----------------------------------------------

print("\n--- Checking Keys ---")

data = {"a": 1, "b": 2, "c": 3}

# Using "in" to check if key exists
print("a in data:", "a" in data)    # True
print("x in data:", "x" in data)    # False

# get() - returns default if key not found
print(data.get("a", 0))    # 1 (key exists)
print(data.get("x", 0))    # 0 (key missing, returns default)

# Safer than data["x"] which raises KeyError

# -----------------------------------------------
# SECTION 4: Dictionary Methods
# -----------------------------------------------

print("\n--- Dictionary Methods ---")

inventory = {"apples": 5, "bananas": 8, "oranges": 3}

# keys() - all keys
print("Keys:", list(inventory.keys()))

# values() - all values
print("Values:", list(inventory.values()))

# items() - all key-value tuples
print("Items:", list(inventory.items()))

# Iterate over key-value pairs
for fruit, count in inventory.items():
    print(f"  {fruit}: {count}")

# -----------------------------------------------
# SECTION 5: Counting Pattern
# -----------------------------------------------

print("\n--- Counting with Dictionaries ---")

# Classic counting pattern from the course
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]

counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

print("Word counts:", counts)

# Shorter version using get()
counts2 = {}
for word in words:
    counts2[word] = counts2.get(word, 0) + 1
print("Using get():", counts2)

# -----------------------------------------------
# SECTION 6: Counting Word Frequency in Text
# -----------------------------------------------

print("\n--- Word Frequency in Text ---")

text = """to be or not to be that is the question
whether tis nobler in the mind to suffer the
slings and arrows of outrageous fortune or to take
arms against a sea of troubles"""

word_count = {}
for line in text.split("\n"):
    for word in line.split():
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1

print("Top words:")
# Sort by count descending
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:10]:
    print(f"  {word!r:15} {count}")

# -----------------------------------------------
# SECTION 7: Finding Most Common Item
# -----------------------------------------------

print("\n--- Finding Most Common ---")

votes = {"Alice": 45, "Bob": 38, "Charlie": 52, "Diana": 41}

# Find candidate with most votes
winner = None
most_votes = 0
for candidate, count in votes.items():
    if count > most_votes:
        most_votes = count
        winner = candidate

print(f"Winner: {winner} with {most_votes} votes")

print("\n" + "="*50)
print("Chapter 9 Complete!")
print("="*50)