# Chapter 35: Function Composition

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:39:57

## Overview
Function composition is the process of combining two or more functions where the output of one becomes the input of the next. It is a fundamental concept in functional programming.

## Mathematical Notation
compose(f, g)(x) = f(g(x))

## Benefits
- Build complex behavior from simple functions
- Reuse small, focused functions
- Easier to read and test individual steps
- Pipeline data through transformations

## Tools in Python
- Manual composition
- functools.reduce for composing many functions
- toolz/cytoolz libraries (third-party)

## Learning Outcomes
- Compose functions manually
- Build compose() and pipe() utilities
- Create data processing pipelines
- Apply function composition in practice