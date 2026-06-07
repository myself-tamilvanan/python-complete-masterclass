# Chapter 23: OOP - Constructors in Python

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 05:19:47

## Overview
A constructor is a special method called automatically when an object is created. Python provides __init__ (initializer) and __new__ (true constructor).

## Types of Constructors
| Constructor      | Purpose                                  |
|-----------------|------------------------------------------|
| __new__(cls)    | Creates the instance (rarely overridden) |
| __init__(self)  | Initializes the instance (most common)   |

## Constructor Types by Arguments
- **Default constructor**: No parameters (besides self)
- **Parameterized constructor**: Takes one or more parameters
- **Non-parameterized**: Explicitly defined with no args

## Key Concepts
- `self` refers to the current instance
- `__init__` is called every time an object is created
- `__new__` actually creates the object; `__init__` initializes it
- Use `__del__` for cleanup (destructor)
- `super().__init__()` calls the parent class constructor

## Learning Outcomes
- Write parameterized constructors
- Use super() in inheritance chains
- Understand __new__ vs __init__
- Implement __del__ for cleanup