# Chapter 11: Regular Expressions
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import re  # Import the regular expressions module

# -----------------------------------------------
# SECTION 1: Basic Pattern Matching
# -----------------------------------------------

print("--- Basic Pattern Matching ---")

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# re.search() - find if pattern exists anywhere in string
if re.search("From:", line):
    print("Found From: in line")
else:
    print("No match")

# Returns None if no match
result = re.search("xyz", line)
print("Search for xyz:", result)  # None

# -----------------------------------------------
# SECTION 2: Special Characters
# -----------------------------------------------

print("\n--- Special Characters ---")

lines = [
    "From: stephen@example.com",
    "X-From: info@example.com",
    "From stephen@uct.ac.za",
    "Subject: Hello",
]

# ^ anchors to start of string
print("Lines starting with From:")
for line in lines:
    if re.search("^From", line):
        print(" ", line)

# -----------------------------------------------
# SECTION 3: Character Classes
# -----------------------------------------------

print("\n--- Character Classes ---")

test_lines = ["Hello World 123", "Python 3.9 is great", "No numbers here", "42 is the answer"]

# \d matches any digit
for line in test_lines:
    if re.search("\d", line):
        print("Has digit:", line)

# -----------------------------------------------
# SECTION 4: Extracting Data with findall()
# -----------------------------------------------

print("\n--- findall() ---")

# findall() returns ALL matches as a list
text = "Prices: $12.99, $45.00, $3.50 and $199.99"

# Find all numbers with decimal point
prices = re.findall("\d+\.\d+", text)
print("Prices found:", prices)

# Find all email addresses
email_text = "Contact us at info@example.com or support@test.org"
emails = re.findall("[a-zA-Z0-9._]+@[a-zA-Z0-9.]+", email_text)
print("Emails:", emails)

# -----------------------------------------------
# SECTION 5: Groups with Parentheses
# -----------------------------------------------

print("\n--- Capturing Groups ---")

# Parentheses create capturing groups
# findall returns only the group content
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# Extract just the email address
emails = re.findall("[a-zA-Z0-9.]+@[a-zA-Z0-9.]+", line)
print("Email:", emails)

# Extract domain from email
domains = re.findall("@([a-zA-Z0-9.]+)", line)
print("Domain:", domains)

# -----------------------------------------------
# SECTION 6: Greedy vs. Non-Greedy
# -----------------------------------------------

print("\n--- Greedy vs. Non-Greedy ---")

html = "<b>Hello</b> and <i>World</i>"

# Greedy: matches as much as possible
greedy = re.findall("<.*>", html)
print("Greedy:", greedy)

# Non-greedy: add ? to make lazy
non_greedy = re.findall("<.*?>", html)
print("Non-greedy:", non_greedy)

# -----------------------------------------------
# SECTION 7: Practical - Parse Email Log
# -----------------------------------------------

print("\n--- Parsing Email Log ---")

log_lines = [
    "From alice@example.com Mon Jan  5 09:14:16 2024",
    "X-Spam: No",
    "From bob@test.org Tue Jan  6 10:22:30 2024",
    "Subject: Test email",
    "From charlie@domain.net Wed Jan  7 08:00:00 2024",
]

senders = []
for line in log_lines:
    # Match "From" lines and extract email
    match = re.search("^From ([a-zA-Z0-9._]+@[a-zA-Z0-9.]+)", line)
    if match:
        senders.append(match.group(1))  # group(1) is first capture group

print("Senders:", senders)

print("\n" + "=" * 50)
print("Chapter 11 Complete!")
print("=" * 50)
