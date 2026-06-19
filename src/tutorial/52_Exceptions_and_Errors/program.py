# Chapter 52: Exceptions and Errors
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

# -----------------------------------------------
# SECTION 1: Basic try/except
# -----------------------------------------------

print("--- try/except ---")

# Without try/except: program crashes
# x = 1 / 0   # ZeroDivisionError

# With try/except: handle gracefully
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")

try:
    my_list = [1, 2, 3]
    item = my_list[5]
except IndexError as e:
    print(f"IndexError: {e}")

# -----------------------------------------------
# SECTION 2: Multiple except Clauses
# -----------------------------------------------

print("\n--- Multiple Exceptions ---")


def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Both arguments must be numbers!")
    return None


print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error message
print(divide(10, "hello"))  # Error message

# Catch multiple in one except
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")

# Catch any exception
try:
    result = 10 / 0
except Exception as e:
    print(f"Exception type: {type(e).__name__}, Message: {e}")

# -----------------------------------------------
# SECTION 3: else and finally
# -----------------------------------------------

print("\n--- else and finally ---")

try:
    x = int("10")
    print("Success:", x)
except ValueError:
    print("ValueError!")
else:
    # Only runs if NO exception was raised
    print("else block: no exception occurred")
finally:
    # ALWAYS runs - cleanup code
    print("finally block: always executes")

# -----------------------------------------------
# SECTION 4: Raising Exceptions
# -----------------------------------------------

print("\n--- Raising Exceptions ---")


def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    return age


try:
    validate_age(25)
    print("Age 25 is valid")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    validate_age("old")
except TypeError as e:
    print(f"TypeError: {e}")

# -----------------------------------------------
# SECTION 5: Custom Exception Classes
# -----------------------------------------------

print("\n--- Custom Exceptions ---")


# Inherit from Exception or a subclass
class CustomError(Exception):
    pass


class ValueTooHighError(Exception):
    def __init__(self, message, value, max_value):
        super().__init__(message)
        self.value = value
        self.max_value = max_value


class ValueTooLowError(Exception):
    pass


def process_value(val):
    if val > 100:
        raise ValueTooHighError(f"{val} exceeds maximum of 100", val, 100)
    if val < 0:
        raise ValueTooLowError(f"{val} is below minimum of 0")
    return val * 2


try:
    result = process_value(150)
except ValueTooHighError as e:
    print(f"Too high: {e} (value={e.value}, max={e.max_value})")
except ValueTooLowError as e:
    print(f"Too low: {e}")

try:
    result = process_value(50)
    print("Result:", result)
except (ValueTooHighError, ValueTooLowError) as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("Chapter 52 Complete!")
print("=" * 50)
