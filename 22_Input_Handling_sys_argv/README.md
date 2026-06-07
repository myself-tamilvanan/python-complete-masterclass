# Chapter 22: Input Handling with sys.argv

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:28:28

## Overview
Python programs can accept input from multiple sources: interactive console (input()), command-line arguments (sys.argv), environment variables, and the argparse module.

## sys.argv
- `sys.argv` is a list of command-line arguments passed to the script
- `sys.argv[0]` is always the script name
- `sys.argv[1]` is the first user argument, etc.
- All values are **strings** — convert as needed

## Example Usage
```bash
python3 program.py Alice 30
# sys.argv = ["program.py", "Alice", "30"]
```

## argparse Module
- More powerful than sys.argv
- Automatically generates --help
- Supports required/optional args, types, defaults
- Validates input automatically

## Input Sources Comparison
| Source          | Use Case                              |
|-----------------|---------------------------------------|
| input()         | Interactive programs                  |
| sys.argv        | Simple command-line scripts           |
| argparse        | Professional CLI tools                |
| os.environ      | Configuration, secrets, API keys      |
| config files    | Complex configuration                 |

## Learning Outcomes
- Use sys.argv to receive command-line arguments
- Build CLI tools with argparse
- Read environment variables with os.environ
- Validate and process user input safely