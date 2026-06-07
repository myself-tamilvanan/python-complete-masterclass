# Chapter 7: Reading Files
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import os

# -----------------------------------------------
# SECTION 1: Creating a Sample File for Testing
# -----------------------------------------------

# Create a sample file to work with
sample_content = """From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.90])
From: stephen.marquard@uct.ac.za
Date: Sat, 5 Jan 2008 09:14:16 +0200
Subject: [sakai] svn commit: r39772
From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008
From: david.horwitz@uct.ac.za
Date: Fri, 4 Jan 2008 07:02:32 +0200
Subject: [sakai] svn commit: r39771
"""

# Write sample file
with open("mbox-sample.txt", "w") as f:
    f.write(sample_content)
print("Created mbox-sample.txt")

# -----------------------------------------------
# SECTION 2: Opening and Reading a File
# -----------------------------------------------

print("\n--- Opening and Reading ---")

# Open file for reading
fhand = open("mbox-sample.txt")

# Read entire file as one string
content = fhand.read()
print("File size:", len(content), "characters")
fhand.close()  # Always close when done

# -----------------------------------------------
# SECTION 3: Reading Line by Line
# -----------------------------------------------

print("\n--- Reading Line by Line ---")

# for loop iterates over lines in a file
line_count = 0
for line in open("mbox-sample.txt"):
    line_count += 1
print("Total lines:", line_count)

# -----------------------------------------------
# SECTION 4: Searching in a File
# -----------------------------------------------

print("\n--- Searching in File ---")

# Find lines that start with "From:"
for line in open("mbox-sample.txt"):
    line = line.strip()   # Remove whitespace and newline
    if line.startswith("From:"):
        print(line)

# -----------------------------------------------
# SECTION 5: Counting Matching Lines
# -----------------------------------------------

print("\n--- Counting Matches ---")

count = 0
for line in open("mbox-sample.txt"):
    line = line.rstrip()   # Strip right whitespace
    if "From" in line:
        count += 1
print("Lines containing From:", count)

# -----------------------------------------------
# SECTION 6: with Statement (Best Practice)
# -----------------------------------------------

print("\n--- with Statement ---")

# with automatically closes file even if error occurs
with open("mbox-sample.txt", "r") as fhand:
    for line in fhand:
        line = line.strip()
        if line.startswith("Subject:"):
            print(line)

# -----------------------------------------------
# SECTION 7: Writing to a File
# -----------------------------------------------

print("\n--- Writing to a File ---")

# Write mode creates new file (or overwrites existing)
with open("output.txt", "w") as fout:
    fout.write("Hello, File!\n")
    fout.write("This is line 2\n")
    fout.write("This is line 3\n")

# Verify by reading back
with open("output.txt", "r") as fin:
    print(fin.read())

# -----------------------------------------------
# SECTION 8: Append to a File
# -----------------------------------------------

print("\n--- Appending to File ---")

# Append mode adds to end without overwriting
with open("output.txt", "a") as fout:
    fout.write("This is appended line\n")

with open("output.txt") as fin:
    print(fin.read())

# Clean up sample files
os.remove("mbox-sample.txt")
os.remove("output.txt")

print("\n" + "="*50)
print("Chapter 7 Complete!")
print("="*50)