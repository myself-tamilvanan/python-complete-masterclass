# Chapter 26: OOP - Access Specifiers

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:12:48

## Overview
Access specifiers control the visibility and accessibility of class attributes and methods. Python uses naming conventions (not strict enforcement like Java/C++).

## Access Levels in Python
| Level     | Convention       | Access                              |
|-----------|-----------------|--------------------------------------|
| Public    | name            | Accessible from anywhere             |
| Protected | _name           | Convention: use only within class/subclasses |
| Private   | __name          | Name-mangled: _ClassName__name       |

## Name Mangling
- `__name` becomes `_ClassName__name` internally
- This prevents accidental override in subclasses
- Can still be accessed externally with the mangled name (but should not be)

## Python Philosophy
"We are all consenting adults here" — Python trusts developers.
There is no true private access; conventions are used instead.

## Best Practices
- Use public attributes for things that form the public interface
- Use _protected for internal implementation details
- Use __private for truly internal class data that should not be overridden
- Use @property for controlled access to private attributes

## Learning Outcomes
- Understand Python access conventions
- Use _ and __ prefixes appropriately
- Implement @property for getter/setter patterns
- Apply name mangling concepts