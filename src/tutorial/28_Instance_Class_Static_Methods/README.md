# Chapter 28: Instance vs Class vs Static Methods

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:38:27

## Overview
Python classes support three types of methods, each serving a different purpose and receiving different implicit first arguments.

## Method Types
| Type           | Decorator      | First Arg | Access                     |
|----------------|----------------|-----------|----------------------------|
| Instance method| (none)         | self      | Can access instance + class |
| Class method   | @classmethod   | cls       | Can access class only      |
| Static method  | @staticmethod  | (none)    | Cannot access class/instance|

## When to Use Each
- **Instance method**: Needs to access or modify instance state (self.x)
- **Class method**: Factory methods, alternative constructors, class-level state
- **Static method**: Utility functions related to the class, no state needed

## Key Use Cases
- `@classmethod` as alternative constructor: `Date.from_string("2024-01-15")`
- `@staticmethod` for pure utility: `MathHelper.is_prime(17)`
- Instance methods for all normal behavior

## Learning Outcomes
- Know when to use each method type
- Create factory methods with @classmethod
- Write utility functions with @staticmethod
- Design clean class interfaces