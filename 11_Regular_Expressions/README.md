# Chapter 11: Regular Expressions

## Overview
Regular expressions (regex) are a powerful tool for pattern matching and text processing. Python's `re` module provides full regex support.

## Topics Covered
- The re module
- Basic pattern matching with search()
- Extracting data with findall()
- Greedy vs. non-greedy matching
- Special characters and character classes
- Anchors (^ and $)
- String parsing with regex

## Key Concepts
- **Pattern**: A sequence of characters defining a search template
- **Match**: When a pattern is found in a string
- **Group**: A captured portion of a match
- **Greedy**: Match as much as possible (default)
- **Non-greedy**: Match as little as possible (use ?)

## Video Timestamps
- 5:54:56 - Regular Expressions
- 6:05:21 - From Matching to Extracting
- 6:13:47 - String Parsing with Regex

## Common Regex Patterns
| Pattern | Matches                           |
|---------|-----------------------------------|
| .       | Any character except newline      |
| ^       | Start of string                   |
| $       | End of string                     |
| *       | 0 or more of previous             |
| +       | 1 or more of previous             |
| ?       | 0 or 1 of previous                |
| [abc]   | Any of a, b, or c                 |
| [a-z]   | Any lowercase letter              |
| \d      | Any digit (0-9)                   |
| \w      | Word character (letters+digits+_) |
| \s      | Whitespace character              |

## Learning Outcomes
- Use re.search() to find patterns
- Use re.findall() to extract data
- Apply regex for parsing email, URLs, numbers