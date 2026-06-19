# Chapter 20: Operators in Python

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 02:13:16

## Overview
Operators are special symbols that perform operations on variables and values. Python has a rich set of operators covering arithmetic, comparison, logical, bitwise, membership, identity, and assignment operations.

## Types of Operators

### 1. Arithmetic Operators
| Operator | Name            | Example   | Result |
|----------|-----------------|-----------|--------|
| +        | Addition        | 5 + 3     | 8      |
| -        | Subtraction     | 5 - 3     | 2      |
| *        | Multiplication  | 5 * 3     | 15     |
| /        | Division        | 10 / 3    | 3.333  |
| //       | Floor Division  | 10 // 3   | 3      |
| %        | Modulo          | 10 % 3    | 1      |
| **       | Exponentiation  | 2 ** 8    | 256    |

### 2. Comparison Operators
| Operator | Meaning               |
|----------|-----------------------|
| ==       | Equal to              |
| !=       | Not equal to          |
| >        | Greater than          |
| <        | Less than             |
| >=       | Greater than or equal |
| <=       | Less than or equal    |

### 3. Logical Operators
| Operator | Description                      |
|----------|----------------------------------|
| and      | True if both operands are True   |
| or       | True if at least one is True     |
| not      | Reverses the boolean value       |

### 4. Bitwise Operators
| Operator | Name         | Example   |
|----------|--------------|-----------|
| &        | AND          | 5 & 3 = 1 |
| \|       | OR           | 5 \| 3 = 7|
| ^        | XOR          | 5 ^ 3 = 6 |
| ~        | NOT          | ~5 = -6   |
| <<       | Left shift   | 5 << 1 = 10|
| >>       | Right shift  | 5 >> 1 = 2|

### 5. Assignment Operators
`=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=`

### 6. Identity Operators
- `is` : True if both variables point to the same object
- `is not` : True if they point to different objects

### 7. Membership Operators
- `in` : True if value is in sequence
- `not in` : True if value is NOT in sequence

## Operator Precedence (High to Low)
`** > +x,-x,~x > *,/,//,% > +,- > <<,>> > & > ^ > | > Comparisons > not > and > or`

## Learning Outcomes
- Use all Python operator types correctly
- Understand operator precedence
- Apply bitwise operators for low-level operations
- Use augmented assignment operators