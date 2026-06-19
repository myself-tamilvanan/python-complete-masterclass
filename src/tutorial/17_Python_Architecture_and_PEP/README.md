# Chapter 17: Python Architecture & PEP Standards

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50
Timestamps: 00:55:25 Python Architecture | 01:34:15 What is PEP?

## Overview
Understanding how Python works internally (compilation and execution pipeline) and what PEP (Python Enhancement Proposals) standards are — the style guidelines every Python developer should follow.

## Python Architecture
When you run a `.py` file, Python goes through these steps:
1. **Source Code (.py)** → You write human-readable Python code
2. **Compiler** → Python's compiler converts source to Bytecode
3. **Bytecode (.pyc)** → Stored in `__pycache__/` folder, platform-independent
4. **Python Virtual Machine (PVM)** → Executes bytecode line by line
5. **Output** → Results displayed on screen

### Key Components
- **CPython**: The default and most widely used Python interpreter (written in C)
- **PyPy**: JIT-compiled Python (faster for long-running programs)
- **Jython**: Python on Java Virtual Machine
- **IronPython**: Python on .NET framework
- **Bytecode**: Intermediate representation, NOT machine code
- **PVM**: Python Virtual Machine — the engine that runs bytecode
- **GIL (Global Interpreter Lock)**: Only one thread runs Python bytecode at a time in CPython

## What is PEP?
PEP = Python Enhancement Proposal
PEPs are design documents that provide information or describe new features for Python.

### Most Important PEPs
| PEP | What it defines |
|-----|----------------|
| PEP 8  | Style Guide for Python Code (most important for developers) |
| PEP 20 | The Zen of Python (import this) |
| PEP 257 | Docstring Conventions |
| PEP 484 | Type Hints |
| PEP 526 | Variable Annotations |
| PEP 572 | Walrus Operator (:=) |

## PEP 8 Key Rules
- Indentation: 4 spaces (not tabs)
- Max line length: 79 characters
- Two blank lines between top-level functions/classes
- One blank line between methods inside a class
- Imports at the top of the file
- Use snake_case for functions and variables
- Use PascalCase (CamelCase) for class names
- Use UPPER_CASE for constants

## Learning Outcomes
- Understand how Python compiles and executes code
- Know what bytecode and PVM are
- Follow PEP 8 style guidelines in your code
- Use tools like pylint and flake8 for PEP 8 checking