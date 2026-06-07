# Chapter 29: Database Connection with Secure Password

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 07:27:35

## Overview
Connecting to databases securely is critical in production. Never hardcode credentials.

## Security Best Practices
1. Never hardcode passwords in source code
2. Use environment variables for credentials
3. Use .env files with python-dotenv for local development
4. Use parameterized queries to prevent SQL injection
5. Always close connections (use context managers)
6. Hash passwords with salt before storing

## Database Libraries
| Database    | Library              | Install                   |
|-------------|---------------------|---------------------------|
| SQLite      | sqlite3 (built-in)  | (none needed)             |
| PostgreSQL  | psycopg2            | pip install psycopg2      |
| MySQL       | mysql-connector     | pip install mysql-connector-python |
| Any DB      | SQLAlchemy (ORM)    | pip install sqlalchemy    |

## SQL Injection Prevention
ALWAYS use parameterized queries:
- BAD:  "SELECT * FROM users WHERE name = " + user_input
- GOOD: "SELECT * FROM users WHERE name = ?", (user_input,)

## Learning Outcomes
- Store database credentials securely via environment variables
- Use parameterized queries to prevent SQL injection
- Hash and salt passwords properly
- Implement connection management with context managers