# Chapter 24: OOP - Polymorphism

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 05:57:30

## Overview
Polymorphism means "many forms." It allows different classes to be treated as instances of the same class through a common interface. One method name, different behaviors.

## Types of Polymorphism
1. **Method Overriding (Runtime Polymorphism)**: Child class overrides parent method
2. **Duck Typing**: "If it walks like a duck and quacks like a duck, it is a duck"
3. **Operator Overloading**: Redefine operators for custom classes
4. **Function Overloading**: Python uses default args instead (no true overloading)

## Key Concepts
- **Override**: A child class provides its own implementation of a parent method
- **Duck typing**: Python checks for methods/attributes, not types
- **isinstance()**: Check if object is an instance of a class
- **Dunder methods**: __add__, __len__, __str__ etc. enable operator overloading

## Benefits
- Write more generic, reusable code
- Extend functionality without modifying existing code
- Follow the Open/Closed Principle (open for extension, closed for modification)

## Learning Outcomes
- Override parent class methods effectively
- Use duck typing for flexible code
- Implement operator overloading with dunder methods
- Write polymorphic functions