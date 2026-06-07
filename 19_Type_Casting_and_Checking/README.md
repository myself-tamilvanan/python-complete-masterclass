# Chapter 19: Type Casting & Type Checking

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:04:35

## Overview
Type casting converts a value from one data type to another. Type checking verifies what type a value is. Both are essential for writing correct, robust Python programs.

## Type Casting (Type Conversion)
### Implicit Conversion (Python does it automatically)
- Python automatically converts compatible types when needed
- Example: int + float → float

### Explicit Conversion (You do it manually)
| Function  | Converts to   | Example             |
|-----------|--------------|---------------------|
| int()     | Integer       | int("42") → 42      |
| float()   | Float         | float("3.14") → 3.14|
| str()     | String        | str(42) → "42"      |
| bool()    | Boolean       | bool(0) → False     |
| list()    | List          | list("abc") → ["a","b","c"] |
| tuple()   | Tuple         | tuple([1,2]) → (1,2)|
| set()     | Set           | set([1,1,2]) → {1,2}|
| dict()    | Dictionary    | dict(a=1) → {"a":1} |
| bytes()   | Bytes         | bytes("hi","utf-8") |

## Type Checking
| Method          | Use case                             |
|-----------------|--------------------------------------|
| type(x)         | Returns exact type of x              |
| isinstance(x,T) | Returns True if x is instance of T   |
| issubclass(A,B) | Returns True if A is subclass of B   |

## Type Hints (PEP 484)
- Python 3.5+ supports type hints for documentation and static analysis
- Tools like mypy can check type hints statically

## Learning Outcomes
- Convert between Python data types safely
- Check types using type() and isinstance()
- Add type hints to function signatures
- Handle conversion errors with try/except