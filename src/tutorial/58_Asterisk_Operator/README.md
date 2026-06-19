# Chapter 58: The Asterisk (*) Operator

## Overview
The asterisk (*) operator has multiple uses in Python beyond just multiplication: unpacking, collecting, and function argument syntax.

## Topics Covered
- Multiplication and power operators
- *args in function definitions
- **kwargs in function definitions
- Unpacking iterables with *
- Unpacking dicts with **
- Forcing keyword-only arguments
- Asterisk in assignments (extended unpacking)

## Key Concepts
- **Unpack (*)**: Expands an iterable into individual elements
- **Collect (*)**: In function signatures, collects multiple args into tuple
- **Merge (**)**: Merges dictionaries or passes them as keyword args
- **Keyword-only (*)**: Everything after bare * must be keyword argument

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 5:17:28)

## All Uses of * and **
| Usage                | Meaning                              |
|----------------------|--------------------------------------|
| a * b                | Multiplication                       |
| a ** b               | Exponentiation                       |
| def f(*args)         | Collect positional args as tuple     |
| def f(**kwargs)      | Collect keyword args as dict         |
| f(*list)             | Unpack list as positional args       |
| f(**dict)            | Unpack dict as keyword args          |
| a, *b = [1,2,3,4]   | Extended unpacking                   |
| def f(a, *, b)       | b is keyword-only                    |

## Learning Outcomes
- Use * and ** for unpacking and collecting
- Force keyword-only arguments with *
- Merge data structures with **
- Master extended unpacking
