# Chapter 33: Closure Functions
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:21:12
# ============================================

# -----------------------------------------------
# SECTION 1: Basic Closure
# -----------------------------------------------

print("--- Basic Closure ---")


def outer(message):
    """Outer function defines message."""

    def inner():
        """Inner function CLOSES OVER message from outer."""
        print("Message:", message)

    return inner  # Return function, not result!


# Create closures with different messages
say_hello = outer("Hello!")
say_goodbye = outer("Goodbye!")

say_hello()  # Uses the captured "Hello!"
say_goodbye()  # Uses the captured "Goodbye!"

# -----------------------------------------------
# SECTION 2: Counter Closure
# -----------------------------------------------

print("\n--- Counter Closure ---")


def make_counter(start=0, step=1):
    """Create a counter that remembers its state."""
    count = [start]  # Use list to allow mutation in closure

    def counter():
        val = count[0]
        count[0] += step
        return val

    return counter


counter1 = make_counter()
counter2 = make_counter(10, 5)  # Start at 10, step by 5

print(counter1())  # 0
print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 10
print(counter2())  # 15
print(counter1())  # 3 - independent state!

# -----------------------------------------------
# SECTION 3: Closure with nonlocal
# -----------------------------------------------

print("\n--- nonlocal in Closures ---")


def make_account(initial_balance):
    """Bank account using closures."""
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Amount must be positive")
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        return balance

    def get_balance():
        return balance

    return {"deposit": deposit, "withdraw": withdraw, "balance": get_balance}


acc = make_account(1000)
print("Balance:", acc["balance"]())
acc["deposit"](500)
print("After deposit:", acc["balance"]())
acc["withdraw"](200)
print("After withdraw:", acc["balance"]())

# -----------------------------------------------
# SECTION 4: Inspecting Closures
# -----------------------------------------------

print("\n--- Inspecting Closures ---")


def multiplier(factor):
    def multiply(n):
        return n * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print("double(5):", double(5))
print("triple(5):", triple(5))

# Inspect closure cells
print("Closure vars:", double.__code__.co_freevars)
print("Closure cell:", double.__closure__[0].cell_contents)

print("\n" + "=" * 50)
print("Chapter 33 Complete!")
print("=" * 50)
