# Chapter 32: Lambda, Map, Filter, Reduce

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:15:34

## Overview
Lambda, map, filter, and reduce are the core functional programming tools in Python. They allow concise, declarative data transformation.

## Lambda
- Anonymous, single-expression function
- Syntax: lambda args: expression
- Used where a short function is needed temporarily

## map(func, iterable)
- Applies func to every item
- Returns a map object (lazy iterator)
- Wrap in list() to get all results

## filter(func, iterable)
- Keeps items where func returns True
- Returns a filter object (lazy)

## reduce(func, iterable[, initializer])
- Cumulatively applies func left to right
- From functools module
- Example: reduce(lambda x,y: x+y, [1,2,3,4]) = 10

## Equivalents
| Functional      | Equivalent list comprehension              |
|-----------------|---------------------------------------------|
| map(f, lst)     | [f(x) for x in lst]                        |
| filter(p, lst)  | [x for x in lst if p(x)]                   |

## Learning Outcomes
- Write concise lambda expressions
- Transform data with map()
- Filter data with filter()
- Accumulate data with reduce()