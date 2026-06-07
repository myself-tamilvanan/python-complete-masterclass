# Chapter 39: PyTest Basics
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:53:56
# ============================================
# NOTE: To run these tests, save as test_program.py and run: pytest test_program.py -v

import pytest

# -----------------------------------------------
# SECTION 1: The Code to Test
# -----------------------------------------------

def add(a, b):
    """Add two numbers."""
    return a + b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def is_palindrome(s):
    """Check if string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0: raise ValueError("Amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance: raise ValueError("Insufficient funds")
        self.balance -= amount

# -----------------------------------------------
# SECTION 2: Basic Test Functions
# -----------------------------------------------

def test_add_positive():
    """Test adding positive numbers."""
    result = add(2, 3)
    assert result == 5

def test_add_negative():
    """Test adding negative numbers."""
    assert add(-1, -2) == -3

def test_add_zero():
    """Test adding zero."""
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_divide_normal():
    """Test normal division."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test that division by zero raises exception."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_by_zero_message():
    """Test exception message."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)

# -----------------------------------------------
# SECTION 3: Parametrize - Test Multiple Inputs
# -----------------------------------------------

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (2.5, 2.5, 5.0),
])
def test_add_parametrized(a, b, expected):
    """Test add with multiple inputs."""
    assert add(a, b) == expected

@pytest.mark.parametrize("word,expected", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("python", False),
    ("level", True),
])
def test_palindrome(word, expected):
    assert is_palindrome(word) == expected

# -----------------------------------------------
# SECTION 4: Fixtures
# -----------------------------------------------

@pytest.fixture
def bank_account():
    """Create a fresh BankAccount for each test."""
    return BankAccount(100)

@pytest.fixture
def funded_account():
    """Create an account with 1000 balance."""
    acc = BankAccount()
    acc.deposit(1000)
    return acc

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 150

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 70

def test_withdraw_insufficient(funded_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        funded_account.withdraw(2000)

def test_deposit_invalid(bank_account):
    with pytest.raises(ValueError, match="Amount must be positive"):
        bank_account.deposit(-50)

# -----------------------------------------------
# SECTION 5: Run demo tests inline
# -----------------------------------------------

if __name__ == "__main__":
    print("Running tests manually...")
    
    # Test add
    assert add(2, 3) == 5
    print("test_add: PASSED")
    
    # Test divide
    try:
        divide(10, 0)
        print("test_divide_zero: FAILED (no exception)")
    except ZeroDivisionError:
        print("test_divide_zero: PASSED")
    
    # Test palindrome
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    print("test_palindrome: PASSED")
    
    print("\nAll manual tests passed!")
    print("Run: pytest test_program.py -v for full pytest output")