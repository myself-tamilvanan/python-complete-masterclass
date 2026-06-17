# Chapter 57: Function Arguments (Advanced)

## Overview
Python provides flexible function argument mechanisms including positional, keyword, default, variable-length (*args), and keyword variable-length (**kwargs) arguments.

## Topics Covered
- Positional arguments
- Keyword arguments
- Default arguments
- *args: variable positional arguments
- **kwargs: variable keyword arguments
- Keyword-only arguments
- Positional-only arguments (Python 3.8+)
- Argument ordering rules
- Mutable default argument pitfall

## Key Concepts
- **Positional**: Matched by position
- **Keyword**: Matched by name
- **Default**: Has a value if not provided
- ***args**: Collects extra positional args as tuple
- ****kwargs**: Collects extra keyword args as dict
- **Keyword-only**: Must be specified by name (after * or *args)

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 4:53:26)

## Argument Order in Function Definition
```
def func(pos1, pos2, /, regular, *args, kw_only, **kwargs):
    pass
```
1. Positional-only (before /)
2. Regular (positional or keyword)
3. *args (extra positional)
4. Keyword-only (after *args)
5. **kwargs (extra keyword)

## Learning Outcomes
- Write flexible functions with *args and **kwargs
- Use keyword-only arguments
- Call functions with positional and keyword args
- Unpack sequences and dicts when calling functions
- Avoid mutable default argument bug
