# Chapter 60: Context Managers

## Overview
Context managers handle resource acquisition and release automatically using the `with` statement. They ensure cleanup always happens, even when exceptions occur.

## Topics Covered
- The with statement
- Built-in context managers (open, threading.Lock)
- Creating context managers with __enter__ and __exit__
- Creating context managers with contextlib.contextmanager
- Multiple context managers
- Exception handling in context managers

## Key Concepts
- **Context manager protocol**: __enter__() and __exit__() methods
- **with statement**: Calls __enter__ on entry, __exit__ on exit
- **@contextmanager**: Decorator for generator-based context managers
- **__exit__ parameters**: exc_type, exc_val, exc_tb (None if no exception)
- **Return True from __exit__**: Suppress the exception

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 5:40:07)

## Common Built-in Context Managers
| Context Manager       | Resource managed           |
|-----------------------|----------------------------|
| open()                | File handles               |
| threading.Lock()      | Thread locks               |
| subprocess.Popen()    | Subprocesses               |
| decimal.localcontext()| Decimal context            |

## Learning Outcomes
- Use with statement for resource management
- Create custom context managers with a class
- Create context managers with @contextmanager
- Handle exceptions inside context managers
