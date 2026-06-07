# Chapter 21: Comments & Documentation

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:24:56

## Overview
Good documentation makes code understandable and maintainable. Python supports single-line comments, multi-line comments, and docstrings (PEP 257).

## Types of Comments
| Type            | Syntax       | Use Case                        |
|-----------------|-------------|----------------------------------|
| Single-line     | # comment   | Explain a line or small block    |
| Multi-line      | """..."""    | Longer explanations              |
| Docstring       | """..."""    | Document functions/classes       |
| Inline          | x = 5 # val | Note beside code                 |

## Docstring Formats
1. **Google Style** (recommended)
2. **NumPy Style** (data science)
3. **reStructuredText** (Sphinx documentation)

## Key Principles
- Comments should explain WHY, not WHAT (code should explain what)
- Keep comments up to date with code changes
- Prefer docstrings for functions, classes, and modules
- Use type hints + docstrings together for maximum clarity

## Tools
- `help(func)` — show docstring in REPL
- `func.__doc__` — access docstring programmatically
- `pydoc` — generate HTML documentation
- `Sphinx` — professional documentation generator

## Learning Outcomes
- Write meaningful comments that add value
- Create proper docstrings in Google/NumPy style
- Use pydoc and help() to view documentation
- Generate documentation automatically