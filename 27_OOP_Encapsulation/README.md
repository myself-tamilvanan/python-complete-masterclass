# Chapter 27: OOP - Encapsulation

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:29:56

## Overview
Encapsulation bundles data (attributes) and the methods that operate on that data into a single unit (class), and restricts direct access to some components.

## What Encapsulation Achieves
1. **Data hiding**: Internal state is protected from direct external access
2. **Data validation**: Setters can validate before changing state
3. **Flexibility**: Internal implementation can change without affecting external code
4. **Maintainability**: Changes are isolated within the class

## Encapsulation vs Abstraction
| Encapsulation              | Abstraction                     |
|----------------------------|---------------------------------|
| Hides the DATA             | Hides the IMPLEMENTATION        |
| Controls access            | Shows only the interface         |
| Achieved via access mods   | Achieved via abstract classes    |
| Protects internal state    | Simplifies complexity            |

## Real-World Analogy
- A **capsule** contains medicine — you take the pill without knowing the chemical formula inside
- A **TV remote** — you press buttons without knowing the infrared signals
- A **car** — you use the pedals/wheel without knowing the engine internals

## Learning Outcomes
- Bundle data and methods in a class
- Use @property for getter/setter patterns
- Validate data in setters
- Understand why encapsulation improves software design