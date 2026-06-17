# Chapter 52: Exceptions and Errors

## Overview
Exceptions are events that disrupt the normal flow of a program. Learning to handle them properly makes code robust and user-friendly.

## Topics Covered
- Common built-in exceptions
- try/except/else/finally blocks
- Catching multiple exceptions
- Raising exceptions
- Custom exception classes
- Context managers for cleanup

## Key Concepts
- **Exception**: An error event that interrupts normal flow
- **try**: Block that may raise an exception
- **except**: Handles specific exception types
- **else**: Runs if no exception was raised
- **finally**: Always runs (cleanup)
- **raise**: Manually trigger an exception
- **Custom Exception**: Class inheriting from Exception

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 2:04:03)

## Common Exceptions
| Exception       | When it occurs                      |
|-----------------|-------------------------------------|
| ValueError      | Wrong value type                    |
| TypeError       | Wrong data type                     |
| KeyError        | Dict key not found                  |
| IndexError      | List index out of range             |
| FileNotFoundError | File does not exist              |
| ZeroDivisionError | Division by zero                 |
| AttributeError  | Object has no attribute             |

## Learning Outcomes
- Handle exceptions gracefully
- Create custom exception classes
- Use finally for cleanup code
- Know when to raise exceptions
