# Chapter 18: Variable Scope (LEGB Rule)
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 01:51:12
# ============================================

# -----------------------------------------------
# SECTION 1: Local Scope
# -----------------------------------------------

print("--- Local Scope ---")


def local_example():
    local_var = "I am local"  # Only exists inside this function
    print(local_var)


local_example()
# print(local_var)   # NameError: not defined outside function

# -----------------------------------------------
# SECTION 2: Global Scope
# -----------------------------------------------

print("\n--- Global Scope ---")

global_var = "I am global"


def read_global():
    # Can READ global variable without declaring
    print("Inside function:", global_var)


read_global()
print("Outside function:", global_var)

# PROBLEM: Assigning to a global inside function creates LOCAL copy
counter = 0


def increment_wrong():
    counter = 10  # This creates a NEW local variable!
    print("Inside (wrong):", counter)


increment_wrong()
print("Global counter unchanged:", counter)  # Still 0


# SOLUTION: Use global keyword
def increment_correct():
    global counter
    counter += 1
    print("Inside (correct):", counter)


increment_correct()
increment_correct()
print("Global counter now:", counter)  # 2

# -----------------------------------------------
# SECTION 3: Enclosing Scope (Closures)
# -----------------------------------------------

print("\n--- Enclosing Scope ---")


def outer():
    x = "outer variable"

    def inner():
        print("inner sees:", x)  # x from enclosing scope

    inner()


outer()


# Modifying enclosing variable with nonlocal
def counter_factory():
    count = 0

    def increment():
        nonlocal count  # Refers to count in outer()
        count += 1
        return count

    return increment


my_counter = counter_factory()
print("count:", my_counter())  # 1
print("count:", my_counter())  # 2
print("count:", my_counter())  # 3

# -----------------------------------------------
# SECTION 4: Built-in Scope
# -----------------------------------------------

print("\n--- Built-in Scope ---")

# Built-in names are always available
print(len([1, 2, 3]))  # len is built-in
print(max([5, 3, 9, 1]))  # max is built-in
print(type(42))  # type is built-in

# You can shadow built-ins (avoid this!)
# list = [1, 2, 3]  # BAD: shadows built-in list()
# print(list(range(5)))  # TypeError now!

# -----------------------------------------------
# SECTION 5: LEGB in Action
# -----------------------------------------------

print("\n--- LEGB Resolution ---")

x = "global x"


def outer_func():
    x = "enclosing x"

    def inner_func():
        x = "local x"
        print("Local:", x)  # L - local wins

    def middle_func():
        print("Enclosing:", x)  # E - enclosing (no local x here)

    inner_func()
    middle_func()


outer_func()
print("Global:", x)  # G - global

# -----------------------------------------------
# SECTION 6: Scope in Comprehensions
# -----------------------------------------------

print("\n--- Scope in Comprehensions ---")

# List comprehension has its own scope in Python 3
result = [i * 2 for i in range(5)]
# print(i)   # NameError in Python 3 (i is local to comprehension)

# But for loop leaks the variable
for j in range(5):
    pass
print("j after for loop:", j)  # 4 - accessible!

print("\n" + "=" * 50)
print("Chapter 18 Complete!")
print("=" * 50)
