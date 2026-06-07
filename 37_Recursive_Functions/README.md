# Chapter 37: Recursive Functions

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:45:31

## Overview
Recursion is when a function calls itself. It is a powerful technique for solving problems that can be broken down into smaller versions of the same problem.

## Requirements
Every recursive function needs:
1. **Base case**: The condition when recursion stops
2. **Recursive case**: The function calling itself with smaller input

## Python Recursion Limit
- Default maximum recursion depth: 1000
- Can be changed with sys.setrecursionlimit()
- For deep recursion, prefer iterative or use memoization

## When to Use Recursion
- Tree traversal
- Divide and conquer algorithms
- Mathematical sequences (factorial, fibonacci)
- Directory traversal
- Parsing nested structures

## Recursion vs Iteration
| Recursion              | Iteration               |
|------------------------|-------------------------|
| More elegant/readable  | Usually more efficient  |
| Call stack overhead    | No stack overflow risk  |
| Natural for trees      | Natural for sequences   |

## Learning Outcomes
- Identify base case and recursive case
- Solve classic problems recursively
- Use memoization to optimize recursion
- Know when recursion is appropriate