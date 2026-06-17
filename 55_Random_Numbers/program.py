# Chapter 55: Random Numbers
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import random
import secrets
import string

# -----------------------------------------------
# SECTION 1: Basic Random Functions
# -----------------------------------------------

print("--- Basic Random ---")

# random() - float in [0.0, 1.0)
print("random():", random.random())

# randint(a, b) - int in [a, b] (inclusive)
print("randint(1, 10):", random.randint(1, 10))

# uniform(a, b) - float in [a, b]
print("uniform(1.0, 10.0):", random.uniform(1.0, 10.0))

# randrange(start, stop, step)
print("randrange(0, 10, 2):", random.randrange(0, 10, 2))  # Even number

# -----------------------------------------------
# SECTION 2: Sequence Operations
# -----------------------------------------------

print("\n--- Sequence Operations ---")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# choice() - random single item
print("choice:", random.choice(my_list))

# choices() - k random items WITH replacement
print("choices(k=3):", random.choices(my_list, k=3))

# Weighted choices
outcomes = ["win", "lose", "draw"]
weights = [10, 5, 3]   # win is most likely
result = random.choices(outcomes, weights=weights, k=10)
print("Weighted choices:", result)

# sample() - k random items WITHOUT replacement
print("sample(k=4):", random.sample(my_list, 4))

# shuffle() - shuffle in place
my_list2 = [1, 2, 3, 4, 5]
random.shuffle(my_list2)
print("shuffled:", my_list2)

# -----------------------------------------------
# SECTION 3: Seeds for Reproducibility
# -----------------------------------------------

print("\n--- Seeds ---")

# Setting a seed makes random numbers reproducible
random.seed(42)
print("With seed 42:", random.random())
print("Next:", random.random())

random.seed(42)    # Reset seed
print("Same seed again:", random.random())  # Same as first!
print("Same again:", random.random())       # Same as second!

# -----------------------------------------------
# SECTION 4: Practical Examples
# -----------------------------------------------

print("\n--- Practical Examples ---")

# Dice rolling
def roll_dice(sides=6, num=2):
    return [random.randint(1, sides) for _ in range(num)]

print("Roll 2 dice:", roll_dice())
print("Roll 3d6:", roll_dice(6, 3), "Sum:", sum(roll_dice(6, 3)))

# Card deck
def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    return [f"{v} of {s}" for s in suits for v in values]

deck = create_deck()
random.shuffle(deck)
hand = deck[:5]
print("5-card hand:", hand)

# Random password (NOT secure - use secrets for real passwords)
chars = string.ascii_letters + string.digits
password = "".join(random.choice(chars) for _ in range(10))
print("Random password (not secure):", password)

# -----------------------------------------------
# SECTION 5: secrets Module (Cryptographic)
# -----------------------------------------------

print("\n--- secrets Module ---")

# secrets.randbelow(n) - cryptographically secure
print("secrets.randbelow(100):", secrets.randbelow(100))

# Secure random bytes
token_bytes = secrets.token_bytes(16)
print("Random bytes:", token_bytes.hex())

# Secure URL-safe token
url_token = secrets.token_urlsafe(16)
print("URL token:", url_token)

# Secure hex token (for API keys, passwords)
hex_token = secrets.token_hex(16)
print("Hex token:", hex_token)

# Secure password generation
alphabet = string.ascii_letters + string.digits + "!@#$%"
secure_password = "".join(secrets.choice(alphabet) for _ in range(12))
print("Secure password:", secure_password)

print("\n" + "="*50)
print("Chapter 55 Complete!")
print("="*50)
