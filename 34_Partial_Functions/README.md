# Chapter 34: Partial Functions

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:34:53

## Overview
functools.partial() creates a new function with some arguments pre-filled. This is called partial application and is useful for creating specialized versions of general functions.

## Key Concepts
- **Partial application**: Fix some arguments of a function, creating a new function
- **functools.partial(func, *args, **kwargs)**: Returns a partial object
- **Currying**: Related concept - transform f(a,b,c) into f(a)(b)(c)

## When to Use
- Create specialized versions of general functions
- Reduce repetition when calling the same function with same args repeatedly
- Use with map(), filter() when function needs extra args
- Simplify callback functions

## Learning Outcomes
- Use functools.partial to pre-fill function arguments
- Create specialized functions from general ones
- Understand the difference between partial application and currying