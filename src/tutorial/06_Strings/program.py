# Chapter 6: Strings
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: String Basics
# -----------------------------------------------

print("--- String Basics ---")

# Strings can use single or double quotes
single = "Hello"
double = "World"

# Concatenation
combined = single + " " + double
print(combined)  # Hello World

# String length
print(len(combined))  # 11

# Repetition
print("Ha" * 3)  # HaHaHa

# -----------------------------------------------
# SECTION 2: Indexing
# -----------------------------------------------

print("\n--- Indexing ---")

fruit = "banana"
#          0123456  (indices)

print(fruit[0])  # b  (first character)
print(fruit[1])  # a
print(fruit[-1])  # a  (last character)
print(fruit[-2])  # n  (second to last)

# -----------------------------------------------
# SECTION 3: Slicing
# -----------------------------------------------

print("\n--- Slicing [start:end] ---")

s = "Python Programming"

print(s[0:6])  # Python  (index 0 to 5)
print(s[7:])  # Programming  (from index 7 to end)
print(s[:6])  # Python  (from start to index 5)
print(s[::2])  # every 2nd character
print(s[::-1])  # Reversed string

# -----------------------------------------------
# SECTION 4: String Methods
# -----------------------------------------------

print("\n--- String Methods ---")

text = "  Hello, World!  "

print(text.upper())  # HELLO, WORLD!
print(text.lower())  # hello, world!
print(text.strip())  # "Hello, World!" (no spaces)
print(text.strip().replace(",", ""))

sentence = "the quick brown fox"
print(sentence.capitalize())  # The quick brown fox
print(sentence.title())  # The Quick Brown Fox

# find() returns index of substring, -1 if not found
msg = "Hello, World!"
print(msg.find("World"))  # 7
print(msg.find("xyz"))  # -1

# in operator checks if substring exists
print("World" in msg)  # True
print("xyz" in msg)  # False

# replace(old, new)
print(msg.replace("World", "Python"))  # Hello, Python!

# -----------------------------------------------
# SECTION 5: split() and join()
# -----------------------------------------------

print("\n--- split() and join() ---")

# split() breaks string into list
csv = "apple,banana,cherry,date"
fruits = csv.split(",")  # Split by comma
print(fruits)  # ["apple", "banana", "cherry", "date"]

# split() with no argument splits on whitespace
words = "Hello World Python".split()
print(words)  # ["Hello", "World", "Python"]

# join() combines list into string
joined = " | ".join(fruits)
print(joined)  # apple | banana | cherry | date

# -----------------------------------------------
# SECTION 6: String Formatting
# -----------------------------------------------

print("\n--- String Formatting ---")

name = "Alice"
age = 30
gpa = 3.75

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}, GPA: {gpa:.1f}")

# format() method
print("Name: {}, Age: {}".format(name, age))

# % formatting (older style)
print("Name: %s, Age: %d" % (name, age))

# -----------------------------------------------
# SECTION 7: Practical - Parse a Line
# -----------------------------------------------

print("\n--- Parsing a Line ---")

# Email parsing example from the course
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

if line.startswith("From "):
    parts = line.split()
    email = parts[1]
    domain = email.split("@")[1]
    print("Email:", email)
    print("Domain:", domain)

print("\n" + "=" * 50)
print("Chapter 6 Complete!")
print("=" * 50)
