# Chapter 31: Pure vs Impure Functions

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:10:34

## Overview
Pure and impure functions are core concepts in functional programming. Pure functions are predictable, testable, and safe. Impure functions have side effects.

## Pure Functions
A function is PURE if:
1. Given the same inputs, it ALWAYS returns the same output
2. It has NO side effects (does not modify external state)

## Side Effects (signs of impure functions)
- Modifying a global variable
- Modifying the input argument (mutation)
- Printing to screen
- Writing to a file or database
- Making network requests
- Reading from external state (current time, random numbers)

## Comparison
| Property         | Pure Function     | Impure Function     |
|-----------------|-------------------|---------------------|
| Return value    | Deterministic     | May vary            |
| Side effects    | None              | Has side effects    |
| Testability     | Very easy         | Harder              |
| Debugging       | Easy              | Harder              |
| Caching         | Safe              | Not safe            |

## Learning Outcomes
- Identify pure vs impure functions
- Refactor impure code to be more pure
- Understand benefits of pure functions
- Know when impure functions are necessary