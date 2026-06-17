# Chapter 59: Shallow vs Deep Copying

## Overview
Understanding how Python copies objects is crucial for avoiding subtle bugs. Shallow copies share nested objects while deep copies are fully independent.

## Topics Covered
- Assignment (not a copy at all)
- Shallow copy with copy.copy()
- Deep copy with copy.deepcopy()
- List and dict copy methods
- When shallow vs deep copy matters
- Copying custom objects

## Key Concepts
- **Reference**: Variable pointing to same object in memory
- **Shallow copy**: New container, but nested objects still shared
- **Deep copy**: Completely independent copy at all levels
- **Mutable vs Immutable**: Immutables (int, str) are safe to share

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 5:30:19)

## When to Use Which
| Situation                    | Use                      |
|------------------------------|--------------------------|
| Simple flat objects          | Shallow copy             |
| Nested mutable objects       | Deep copy                |
| Read-only shared data        | Reference (assignment)   |
| Large objects, need clone    | Deep copy                |

## Learning Outcomes
- Understand references vs copies
- Know when shallow copy is enough
- Use deepcopy for nested mutable objects
- Avoid subtle bugs from unexpected sharing
