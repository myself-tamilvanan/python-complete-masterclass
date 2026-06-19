# Chapter 33: Closure Functions

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:21:12

## Overview
A closure is a function that remembers the variables from its enclosing scope even after that scope has finished executing. Closures are the foundation of decorators and functional programming patterns.

## Requirements for a Closure
1. There must be a nested function (function inside a function)
2. The nested function must refer to a variable from the enclosing scope
3. The outer function must return the inner function

## Key Concepts
- **Free variable**: A variable used in a function but defined in the enclosing scope
- **__closure__**: The attribute storing the cell objects of a closure
- **Cell object**: Holds the value of the free variable
- **Enclosing scope**: The scope of the outer function

## Use Cases
- Counter functions
- Memorization without classes
- Decorator factories
- Callbacks with state
- Factory functions

## Learning Outcomes
- Understand how closures capture variables
- Create counter and accumulator functions using closures
- Use closures instead of simple classes
- Debug closures with __closure__ and __code__