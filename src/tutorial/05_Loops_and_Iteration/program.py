# Chapter 5: Loops and Iteration
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

# -----------------------------------------------
# SECTION 1: while Loop (Indefinite Loop)
# -----------------------------------------------

print("--- while Loop ---")

# while loop repeats as long as condition is True
n = 5
while n > 0:
    print("Count:", n)
    n = n - 1  # Decrement to avoid infinite loop
print("Done!")

# -----------------------------------------------
# SECTION 2: Infinite Loop with break
# -----------------------------------------------

print("\n--- break Statement ---")

# Simulate user input loop
inputs = ["hello", "world", "done", "bye"]  # Simulated inputs
i = 0
while True:  # Runs forever until break
    line = inputs[i]
    i += 1
    if line == "done":
        break  # Exit the loop
    print("Input:", line)
print("Loop ended")

# -----------------------------------------------
# SECTION 3: continue Statement
# -----------------------------------------------

print("\n--- continue Statement ---")

# continue skips the rest of loop body for this iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")  # Print odd numbers only
print()  # New line

# -----------------------------------------------
# SECTION 4: for Loop (Definite Loop)
# -----------------------------------------------

print("\n--- for Loop ---")

# for loop iterates over a sequence
friends = ["Alice", "Bob", "Charlie", "Diana"]

for friend in friends:
    print("Hello,", friend)

# -----------------------------------------------
# SECTION 5: range() Function
# -----------------------------------------------

print("\n--- range() Function ---")

# range(stop) - from 0 to stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop) - from start to stop-1
for i in range(2, 8):
    print(i, end=" ")  # 2 3 4 5 6 7
print()

# range(start, stop, step)
for i in range(0, 20, 5):
    print(i, end=" ")  # 0 5 10 15
print()

# -----------------------------------------------
# SECTION 6: Loop Idioms
# -----------------------------------------------

print("\n--- Loop Idioms ---")

numbers = [3, 41, 12, 9, 74, 15]

# COUNTING: count how many items meet a condition
count = 0
for n in numbers:
    if n > 20:
        count += 1
print("Numbers > 20:", count)

# SUMMING: add up all values
total = 0
for n in numbers:
    total += n
print("Sum:", total)

# AVERAGE
print("Average:", total / len(numbers))

# FINDING MAXIMUM
largest = None
for n in numbers:
    if largest is None or n > largest:
        largest = n
print("Largest:", largest)

# FINDING MINIMUM
smallest = None
for n in numbers:
    if smallest is None or n < smallest:
        smallest = n
print("Smallest:", smallest)

# -----------------------------------------------
# SECTION 7: Iterating Over Strings
# -----------------------------------------------

print("\n--- Iterating Over Strings ---")

word = "Python"

# Each character one at a time
for char in word:
    print(char, end="-")
print()

# Count vowels in a string
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print("Vowels in", word + ":", count)

# -----------------------------------------------
# SECTION 8: Nested Loops
# -----------------------------------------------

print("\n--- Nested Loops ---")

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()  # New line after each row

print("\n" + "=" * 50)
print("Chapter 5 Complete!")
print("=" * 50)
