# Chapter 29: Database Connection with Secure Password
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 07:27:35
# ============================================

import hashlib
import os
import secrets
import sqlite3
from contextlib import contextmanager

# -----------------------------------------------
# SECTION 1: Secure Credential Storage
# -----------------------------------------------

print("--- Secure Credential Storage ---")

# BAD - Never hardcode passwords!
# password = "my_secret_password_123"

# GOOD - Use environment variables
db_host = os.environ.get("DB_HOST", "localhost")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "mydb")
db_user = os.environ.get("DB_USER", "admin")
db_password = os.environ.get("DB_PASSWORD", "")

print("DB Config (password masked):")
print("  host:", db_host)
print("  port:", db_port)
print("  name:", db_name)
print("  user:", db_user)
masked = "*" * len(db_password) if db_password else "(not set)"
print("  password:", masked)

# -----------------------------------------------
# SECTION 2: Context Manager for Connections
# -----------------------------------------------

print("\n--- Context Manager ---")


@contextmanager
def get_db_connection(db_path=":memory:"):
    """Context manager - always closes connection."""
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        yield conn
        conn.commit()
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()


with get_db_connection() as conn:
    conn.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, val TEXT)")
    conn.execute("INSERT INTO test (val) VALUES (?)", ("hello",))
    row = conn.execute("SELECT * FROM test").fetchone()
    print("Test row:", dict(row))

# -----------------------------------------------
# SECTION 3: Password Hashing
# -----------------------------------------------

print("\n--- Password Hashing ---")


def hash_password(password):
    """Hash password with random salt using SHA-256."""
    salt = secrets.token_hex(16)
    hash_val = hashlib.sha256((password + salt).encode()).hexdigest()
    return hash_val, salt


def verify_password(password, hash_val, salt):
    """Verify password against stored hash."""
    computed = hashlib.sha256((password + salt).encode()).hexdigest()
    return secrets.compare_digest(computed, hash_val)


pwd = "mySecurePassword123"
h, s = hash_password(pwd)
print("Hash:", h[:20] + "...")
print("Salt:", s)
print("Verify correct password:", verify_password(pwd, h, s))
print("Verify wrong password:", verify_password("wrongpassword", h, s))

# -----------------------------------------------
# SECTION 4: Full User System with SQLite
# -----------------------------------------------

print("\n--- User System with SQLite ---")

with get_db_connection() as conn:
    # Create users table
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL
    )""")

    # Register users with hashed passwords
    users_to_add = [
        ("Alice", "alice@example.com", "alicepass123"),
        ("Bob", "bob@example.com", "bobsecret456"),
    ]
    for name, email, password in users_to_add:
        h, s = hash_password(password)
        # Parameterized query - safe from SQL injection
        conn.execute(
            "INSERT INTO users (name, email, password_hash, salt) VALUES (?, ?, ?, ?)",
            (name, email, h, s),
        )

    # Login verification
    def login(email, password):
        row = conn.execute(
            "SELECT password_hash, salt FROM users WHERE email = ?", (email,)
        ).fetchone()
        if not row:
            return False
        return verify_password(password, row["password_hash"], row["salt"])

    print("alice correct:", login("alice@example.com", "alicepass123"))
    print("alice wrong:", login("alice@example.com", "wrong"))
    print("bob correct:", login("bob@example.com", "bobsecret456"))

print("\n" + "=" * 50)
print("Chapter 29 Complete!")
print("=" * 50)
