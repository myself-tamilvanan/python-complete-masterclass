# Chapter 60: Context Managers
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

from contextlib import contextmanager
import time

# -----------------------------------------------
# SECTION 1: Built-in Context Managers
# -----------------------------------------------

print("--- Built-in Context Managers ---")

# File is automatically closed even if an exception occurs
with open("test.txt", "w") as f:
    f.write("Hello, Context Manager!\n")
    f.write("File will be closed automatically.")

with open("test.txt", "r") as f:
    content = f.read()
print("File content:", content)

# Multiple context managers
with open("test.txt", "r") as fin, open("test_copy.txt", "w") as fout:
    for line in fin:
        fout.write(line)
print("File copied successfully")

# -----------------------------------------------
# SECTION 2: Class-based Context Manager
# -----------------------------------------------

print("\n--- Class-based Context Manager ---")

class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"  Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file  # Assigned to "as" variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  Closing {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"  Exception: {exc_val}")
        return False  # Do not suppress exceptions

with ManagedFile("test.txt", "r") as f:
    print("  Content:", f.read())

# -----------------------------------------------
# SECTION 3: @contextmanager Decorator
# -----------------------------------------------

print("\n--- @contextmanager Decorator ---")

# Simpler way using generators
@contextmanager
def managed_file(filename, mode):
    print(f"  Opening {filename}")
    f = open(filename, mode)
    try:
        yield f   # Control passes to with block here
    finally:
        print(f"  Closing {filename}")
        f.close()  # Always runs

with managed_file("test.txt", "r") as f:
    print("  Content:", f.read())

# -----------------------------------------------
# SECTION 4: Timing Context Manager
# -----------------------------------------------

print("\n--- Timing Context Manager ---")

@contextmanager
def timer(label="Operation"):
    start = time.time()
    print(f"  [{label}] Starting...")
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"  [{label}] Completed in {elapsed:.4f}s")

with timer("Data processing"):
    time.sleep(0.1)
    data = [x**2 for x in range(10000)]

with timer("Sorting"):
    data.sort(reverse=True)

# -----------------------------------------------
# SECTION 5: Exception Handling
# -----------------------------------------------

print("\n--- Exception Handling ---")

class ErrorSuppressor:
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exception_types:
            print(f"  Suppressed {exc_type.__name__}: {exc_val}")
            return True  # Suppress the exception
        return False     # Let other exceptions propagate

# ZeroDivisionError is suppressed
with ErrorSuppressor(ZeroDivisionError, ValueError):
    result = 10 / 0   # Would normally crash
    print("This line is NOT reached")

print("Execution continues after suppressed error")

# ValueError also suppressed
with ErrorSuppressor(ZeroDivisionError, ValueError):
    int("not a number")

print("Still going!")

# Cleanup
import os
for f in ["test.txt", "test_copy.txt"]:
    if os.path.exists(f): os.remove(f)

print("\n" + "="*50)
print("Chapter 60 Complete!")
print("="*50)
