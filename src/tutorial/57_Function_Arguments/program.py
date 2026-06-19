# Chapter 57: Function Arguments (Advanced)
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

# -----------------------------------------------
# SECTION 1: Positional and Keyword Arguments
# -----------------------------------------------

print("--- Positional & Keyword Args ---")


def greet(name, greeting):
    print(f"{greeting}, {name}!")


# Positional: order matters
greet("Alice", "Hello")

# Keyword: order does not matter
greet(greeting="Hi", name="Bob")

# -----------------------------------------------
# SECTION 2: Default Arguments
# -----------------------------------------------

print("\n--- Default Arguments ---")


def power(base, exponent=2, modulo=None):
    result = base**exponent
    if modulo:
        result %= modulo
    return result


print(power(3))  # 9 (default exponent=2)
print(power(2, 10))  # 1024
print(power(2, 10, 100))  # 24


# DANGER: Mutable default arguments!
def append_to(element, lst=[]):  # BAD! Shared across calls
    lst.append(element)
    return lst


print(append_to(1))  # [1]
print(append_to(2))  # [1, 2] - not [2]!


# FIX: Use None as default
def append_to_safe(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst


print(append_to_safe(1))  # [1]
print(append_to_safe(2))  # [2] - correct!

# -----------------------------------------------
# SECTION 3: *args
# -----------------------------------------------

print("\n--- *args ---")


# *args collects extra positional args into a tuple
def sum_all(*args):
    print(f"args = {args}, type = {type(args)}")
    return sum(args)


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6))


# Combine with regular args
def greet_many(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")


greet_many("Hello", "Alice", "Bob", "Charlie")

# -----------------------------------------------
# SECTION 4: **kwargs
# -----------------------------------------------

print("\n--- **kwargs ---")


# **kwargs collects extra keyword args into a dict
def print_info(**kwargs):
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")


print_info(name="Alice", age=30, city="NYC")


# Real-world example: HTML tag builder
def create_tag(tag, content, **attrs):
    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    if attr_str:
        return f"<{tag} {attr_str}>{content}</{tag}>"
    return f"<{tag}>{content}</{tag}>"


print(create_tag("p", "Hello World"))
print(create_tag("a", "Click me", href="http://example.com", target="_blank"))

# -----------------------------------------------
# SECTION 5: Combining all argument types
# -----------------------------------------------

print("\n--- Combining All Types ---")


def complex_func(pos1, pos2, *args, kw_only, **kwargs):
    print(f"pos1={pos1}, pos2={pos2}")
    print(f"args={args}")
    print(f"kw_only={kw_only}")
    print(f"kwargs={kwargs}")


complex_func(1, 2, 3, 4, 5, kw_only="required", extra="hello", more=42)

# -----------------------------------------------
# SECTION 6: Unpacking when Calling
# -----------------------------------------------

print("\n--- Unpacking in Function Calls ---")


def add(a, b, c):
    return a + b + c


# Unpack list/tuple as positional args
my_list = [1, 2, 3]
print(add(*my_list))  # Same as add(1, 2, 3)

# Unpack dict as keyword args
my_dict = {"a": 1, "b": 2, "c": 3}
print(add(**my_dict))  # Same as add(a=1, b=2, c=3)

print("\n" + "=" * 50)
print("Chapter 57 Complete!")
print("=" * 50)
