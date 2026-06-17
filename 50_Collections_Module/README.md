# Chapter 50: Collections Module

## Overview
The collections module provides specialized container datatypes: Counter, namedtuple, OrderedDict, defaultdict, and deque.

## Topics Covered
- Counter: counting hashable objects with most_common()
- namedtuple: tuple with named fields
- OrderedDict: dict remembering insertion order
- defaultdict: dict with automatic default values
- deque: double-ended queue with O(1) operations

## Key Concepts
- **Counter**: dict subclass for counting frequencies
- **defaultdict**: Avoids KeyError with a default factory
- **deque**: O(1) append/pop from both ends (list is O(n) from left)
- **namedtuple**: Lightweight record type with named fields

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 1:22:50)

## Learning Outcomes
- Count elements efficiently with Counter
- Use defaultdict to simplify code
- Use deque for efficient queue and stack operations
- Pick the right collection type for each task
