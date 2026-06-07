# Chapter 10: Tuples
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: Creating Tuples
# -----------------------------------------------

print("--- Creating Tuples ---")

# Tuples use parentheses (optional but conventional)
coordinates = (3, 4)
colors = ("red", "green", "blue")
single = (42,)    # Single-element tuple NEEDS trailing comma
empty = ()        # Empty tuple

print(coordinates)
print(colors)
print(type(single))

# Tuples without parentheses (tuple packing)
point = 10, 20, 30
print(point, type(point))

# -----------------------------------------------
# SECTION 2: Accessing Elements
# -----------------------------------------------

print("\n--- Accessing Elements ---")

rgb = (255, 128, 0)

print(rgb[0])      # 255 (red)
print(rgb[1])      # 128 (green)
print(rgb[-1])     # 0 (blue, last element)
print(rgb[0:2])    # (255, 128) slicing works!

# Tuples are IMMUTABLE - this would cause TypeError:
# rgb[0] = 100   # TypeError!

# -----------------------------------------------
# SECTION 3: Tuple Unpacking
# -----------------------------------------------

print("\n--- Tuple Unpacking ---")

# Assign tuple values to multiple variables
point = (3, 4)
x, y = point      # Unpack into x and y
print("x:", x, "y:", y)

# Useful for swapping variables
a, b = 10, 20
print(f"Before: a={a}, b={b}")
a, b = b, a        # Swap using tuple unpacking
print(f"After swap: a={a}, b={b}")

# Unpack function return values
def get_min_max(nums):
    return min(nums), max(nums)   # Returns a tuple

low, high = get_min_max([3, 1, 4, 1, 5, 9])
print(f"Low: {low}, High: {high}")

# -----------------------------------------------
# SECTION 4: Iterating Over Tuples
# -----------------------------------------------

print("\n--- Iterating Over Tuples ---")

fruits = ("apple", "banana", "cherry")

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# -----------------------------------------------
# SECTION 5: Sorting Dictionaries with Tuples
# -----------------------------------------------

print("\n--- Sorting Dictionaries Using Tuples ---")

word_count = {"banana": 5, "apple": 3, "cherry": 8, "date": 1}

# Convert to list of (key, value) tuples
items = word_count.items()
print("Dict items:", list(items))

# Sort by value (second element of tuple)
sorted_items = sorted(word_count.items(), key=lambda x: x[1])
print("\nSorted by count (ascending):")
for word, count in sorted_items:
    print(f"  {word}: {count}")

# Sort by value descending (most frequent first)
sorted_desc = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("\nSorted by count (descending):")
for word, count in sorted_desc:
    print(f"  {word}: {count}")

# -----------------------------------------------
# SECTION 6: Tuples as Dictionary Keys
# -----------------------------------------------

print("\n--- Tuples as Dictionary Keys ---")

# Lists cannot be dict keys (mutable), but tuples can
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

for coords, city in locations.items():
    lat, lon = coords
    print(f"{city}: lat={lat}, lon={lon}")

print("\n" + "="*50)
print("Chapter 10 Complete!")
print("="*50)