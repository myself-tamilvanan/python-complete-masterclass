# Chapter 18: Variable Scope

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 01:51:12

## Overview
Variable scope defines where a variable can be accessed in your program. Python follows the LEGB rule to determine which variable to use when the same name exists in multiple scopes.

## The LEGB Rule
Python resolves variable names in this order:
1. **L - Local**: Variables defined inside the current function
2. **E - Enclosing**: Variables in enclosing (outer) functions (for closures)
3. **G - Global**: Variables defined at the module level
4. **B - Built-in**: Python built-in names (len, print, range, etc.)

## Scope Keywords
| Keyword    | Purpose                                           |
|------------|---------------------------------------------------|
| global     | Declare that a variable refers to the global scope |
| nonlocal   | Declare that a variable refers to the enclosing scope |

## Key Concepts
- **Local variable**: Exists only inside a function
- **Global variable**: Exists at module level, accessible everywhere
- **Enclosing scope**: The scope of an outer function (used in closures)
- **Built-in scope**: Python's predefined names (always available)
- **Shadow**: When a local variable has the same name as a global, the local "shadows" the global

## Common Mistakes
- Reading a global variable is fine, but **assigning** to it inside a function creates a LOCAL copy unless you use `global`
- Forgetting `nonlocal` in closures causes UnboundLocalError

## Learning Outcomes
- Understand the LEGB scope resolution rule
- Use global and nonlocal keywords correctly
- Avoid variable shadowing bugs
- Design functions with proper scope management