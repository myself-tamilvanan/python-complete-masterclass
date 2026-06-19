# Chapter 56: Decorators

## Overview
Decorators are a powerful Python feature that allow you to modify or extend the behavior of functions or classes without changing their source code. They are widely used in frameworks like Flask and Django.

## Topics Covered
- First-class functions (functions as arguments/return values)
- Closures review
- Creating function decorators
- Decorator with arguments
- functools.wraps
- Class decorators
- Built-in decorators: @property, @staticmethod, @classmethod

## Key Concepts
- **First-class functions**: Functions can be passed as arguments and returned
- **Closure**: A function that remembers variables from its enclosing scope
- **Decorator**: A function that takes a function and returns a modified version
- **@syntax**: Syntactic sugar for applying decorators
- **functools.wraps**: Preserves the wrapped function's metadata

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 3:14:23)

## Common Use Cases
- Timing/profiling functions
- Logging function calls
- Access control / authentication
- Caching / memoization
- Rate limiting

## Learning Outcomes
- Understand first-class functions and closures
- Create decorators to add behavior to functions
- Use functools.wraps correctly
- Apply decorators with arguments
