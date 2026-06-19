# Chapter 30: Higher Order Functions

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 07:53:00

## Overview
A Higher-Order Function (HOF) is a function that either accepts other functions as arguments or returns a function as its result. They are fundamental to functional programming.

## Definition
A function is "higher-order" if it:
1. Takes one or more functions as arguments, OR
2. Returns a function as its result (or both)

## Built-in Higher-Order Functions
| Function   | Description                                     |
|------------|------------------------------------------------|
| map()      | Apply function to every item in iterable        |
| filter()   | Keep items where function returns True          |
| sorted()   | Sort with custom key function                   |
| reduce()   | Cumulatively apply function (functools)         |
| any()      | True if any element satisfies condition         |
| all()      | True if all elements satisfy condition          |

## Benefits
- Code reuse: write generic logic once
- Composition: combine small functions into powerful ones
- Separation of concerns: separate WHAT to do from HOW

## Learning Outcomes
- Write functions that accept other functions
- Return functions from functions
- Use built-in HOFs effectively
- Build function pipelines