# Chapter 55: Random Numbers

## Overview
The random module provides functions for generating pseudo-random numbers. Understanding randomness is important for simulations, games, testing, and cryptography.

## Topics Covered
- random.random(): float between 0 and 1
- random.randint(a, b): integer between a and b
- random.uniform(a, b): float between a and b
- random.choice(): random item from sequence
- random.choices(): weighted random selection
- random.shuffle(): shuffle a list in place
- random.sample(): random subset without replacement
- Setting seeds for reproducibility
- secrets module for cryptographic randomness

## Key Concepts
- **Pseudo-random**: Deterministic but appears random
- **Seed**: Starting point that makes sequence reproducible
- **secrets**: Cryptographically secure random (for passwords, tokens)

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 2:59:42)

## random vs secrets
| random          | secrets                          |
|-----------------|----------------------------------|
| Fast            | Slower                           |
| Reproducible    | Truly unpredictable              |
| Simulations     | Passwords, tokens, security      |

## Learning Outcomes
- Generate random numbers and selections
- Shuffle and sample from sequences
- Set seeds for reproducibility
- Use secrets for security-sensitive code
