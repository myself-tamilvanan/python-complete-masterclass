# Chapter 21: Comments & Documentation
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:24:56
# ============================================

# -----------------------------------------------
# SECTION 1: Single-Line Comments
# -----------------------------------------------

# This is a single-line comment
x = 5  # Inline comment: x is the starting count

# Good comments explain WHY, not what
# BAD: increment counter by 1
# counter += 1

# GOOD: Retry failed requests up to MAX_RETRIES times
MAX_RETRIES = 3
retry_count = 0

# -----------------------------------------------
# SECTION 2: Multi-line Comments
# -----------------------------------------------

"""
This is a multi-line string used as a comment.
It is not assigned to any variable.
Python treats it as an expression and discards it.
Often used for long explanations or TODOs.
"""

# TODO: Implement error handling here
# FIXME: This function is slow for large inputs
# NOTE: This algorithm has O(n log n) complexity
# HACK: Temporary fix, needs refactoring

# -----------------------------------------------
# SECTION 3: Docstrings - One-line
# -----------------------------------------------


def add(a, b):
    """Return the sum of a and b."""
    return a + b


# Access docstring
print("Docstring:", add.__doc__)
help(add)

# -----------------------------------------------
# SECTION 4: Docstrings - Google Style
# -----------------------------------------------


def calculate_compound_interest(principal, rate, time, n=12):
    """
    Calculate compound interest.

    Args:
        principal (float): Initial investment amount in dollars.
        rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
        time (float): Time period in years.
        n (int, optional): Number of times interest is compounded per year.
            Defaults to 12 (monthly).

    Returns:
        float: Final amount after compound interest.

    Raises:
        ValueError: If principal, rate, or time is negative.

    Example:
        >>> calculate_compound_interest(1000, 0.05, 10)
        1647.0090...
    """
    if any(v < 0 for v in [principal, rate, time]):
        raise ValueError("principal, rate, and time must be non-negative")
    return principal * (1 + rate / n) ** (n * time)


result = calculate_compound_interest(1000, 0.05, 10)
print(f"\nCompound interest result: ${result:.2f}")

# -----------------------------------------------
# SECTION 5: Class Docstrings
# -----------------------------------------------


class BankAccount:
    """
    A simple bank account class.

    Attributes:
        owner (str): Name of the account owner.
        balance (float): Current account balance.

    Example:
        >>> account = BankAccount("Alice", 1000)
        >>> account.deposit(500)
        >>> account.balance
        1500
    """

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Initialize a bank account.

        Args:
            owner: Account owner's name.
            balance: Starting balance (default 0.0).
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Deposit money into the account.

        Args:
            amount: Amount to deposit (must be positive).

        Returns:
            New balance after deposit.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance


acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(f"\nBalance: ${acc.balance}")
print("Class docstring:", BankAccount.__doc__[:50])

# -----------------------------------------------
# SECTION 6: Module Docstring
# -----------------------------------------------

# The first statement in a .py file should be the module docstring
# Example (would go at very top of file):
"""
my_module.py

This module provides utilities for financial calculations.

Author: Gowtham
Date: 2024
Version: 1.0
"""

print("\n" + "=" * 50)
print("Chapter 21 Complete!")
print("=" * 50)
