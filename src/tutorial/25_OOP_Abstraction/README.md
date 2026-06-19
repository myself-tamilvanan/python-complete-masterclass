# Chapter 25: OOP - Abstraction

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 06:02:05

## Overview
Abstraction hides implementation details and only exposes the essential interface. In Python, abstraction is achieved using Abstract Base Classes (ABCs) from the `abc` module.

## Key Concepts
- **Abstract Class**: A class that cannot be instantiated directly
- **Abstract Method**: A method declared but not implemented in the abstract class
- **Concrete Class**: A class that implements all abstract methods
- **ABC (Abstract Base Class)**: Python's mechanism for abstraction (from `abc` module)
- **@abstractmethod**: Decorator that marks a method as abstract

## Abstraction vs Encapsulation
| Abstraction           | Encapsulation               |
|-----------------------|-----------------------------|
| Hides complexity      | Hides data                  |
| Shows only interface  | Controls access to data     |
| Achieved via ABCs     | Achieved via access modifiers|

## Real-World Examples
- Car: You use the steering wheel, pedals (interface). The engine mechanics are hidden (abstraction)
- ATM: You use buttons and screen (interface). Internal banking is hidden
- Payment Gateway: process_payment() is the interface; card/UPI logic is hidden

## Learning Outcomes
- Create abstract classes with abc module
- Define abstract methods that subclasses must implement
- Understand when to use abstraction
- Design clean, extensible class hierarchies