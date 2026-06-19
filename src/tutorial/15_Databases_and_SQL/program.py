# Chapter 15: Databases and SQL
# Python for Everybody - freeCodeCamp Course
# Source: https://youtu.be/8DvywoWv6fI
# ============================================

import sqlite3

# -----------------------------------------------
# SECTION 1: Creating a Database and Table
# -----------------------------------------------

print("--- Creating Database ---")

# Connect to database (creates file if not exists)
# Use ":memory:" for in-memory database (no file created)
conn = sqlite3.connect(":memory:")

# Create a cursor to execute SQL
cur = conn.cursor()

# CREATE TABLE - define structure
cur.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
""")

print("Table created successfully")

# -----------------------------------------------
# SECTION 2: Inserting Data
# -----------------------------------------------

print("\n--- Inserting Data ---")

# INSERT INTO - add rows
# Use ? placeholders to prevent SQL injection
users = [
    ("Alice", "alice@example.com", 30),
    ("Bob", "bob@example.com", 25),
    ("Charlie", "charlie@example.com", 35),
    ("Diana", "diana@example.com", 28),
]

cur.executemany(
    """
    INSERT INTO Users (name, email, age) VALUES (?, ?, ?)
""",
    users,
)

# Commit saves changes to database
conn.commit()
print(f"Inserted {len(users)} users")

# -----------------------------------------------
# SECTION 3: Querying Data
# -----------------------------------------------

print("\n--- Querying Data ---")

# SELECT * - get all rows and columns
cur.execute("SELECT * FROM Users")
rows = cur.fetchall()

print("All users:")
for row in rows:
    print(f"  ID:{row[0]} Name:{row[1]} Email:{row[2]} Age:{row[3]}")

# SELECT specific columns
cur.execute("SELECT name, age FROM Users ORDER BY age")
print("\nUsers sorted by age:")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")

# -----------------------------------------------
# SECTION 4: WHERE Clause (Filtering)
# -----------------------------------------------

print("\n--- WHERE Filtering ---")

# Find users over 28
cur.execute("SELECT name, age FROM Users WHERE age > 28")
print("Users older than 28:")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")

# Find user by email (parameterized)
email = "alice@example.com"
cur.execute("SELECT * FROM Users WHERE email = ?", (email,))
result = cur.fetchone()
print(f"\nFound user: {result}")

# -----------------------------------------------
# SECTION 5: UPDATE and DELETE
# -----------------------------------------------

print("\n--- UPDATE and DELETE ---")

# UPDATE - modify existing records
cur.execute("UPDATE Users SET age = ? WHERE name = ?", (31, "Alice"))
conn.commit()

cur.execute("SELECT name, age FROM Users WHERE name = 'Alice'")
print("Alice after update:", cur.fetchone())

# DELETE - remove records
cur.execute("DELETE FROM Users WHERE age < 26")
conn.commit()

cur.execute("SELECT COUNT(*) FROM Users")
print("Users after delete:", cur.fetchone()[0])

# -----------------------------------------------
# SECTION 6: Relationships and JOIN
# -----------------------------------------------

print("\n--- Relationships and JOIN ---")

# Create related tables
cur.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        instructor TEXT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        user_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        PRIMARY KEY (user_id, course_id),
        FOREIGN KEY (user_id) REFERENCES Users(id),
        FOREIGN KEY (course_id) REFERENCES Courses(id)
    )
""")

# Insert courses
courses = [("Python Basics", "Dr. Chuck"), ("Data Science", "Dr. Smith")]
cur.executemany("INSERT INTO Courses (title, instructor) VALUES (?, ?)", courses)

# Enroll users
enrollments = [(1, 1, "A"), (1, 2, "B+"), (2, 1, "A-")]
cur.executemany("INSERT OR IGNORE INTO Enrollments VALUES (?, ?, ?)", enrollments)
conn.commit()

# JOIN query - combine Users and Courses via Enrollments
cur.execute("""
    SELECT u.name, c.title, e.grade
    FROM Users u
    JOIN Enrollments e ON u.id = e.user_id
    JOIN Courses c ON c.id = e.course_id
    ORDER BY u.name
""")

print("Enrollment data (JOIN result):")
for row in cur.fetchall():
    print(f"  {row[0]} enrolled in {row[1]}: {row[2]}")

# Close connection
conn.close()

print("\n" + "=" * 50)
print("Chapter 15 Complete!")
print("=" * 50)
