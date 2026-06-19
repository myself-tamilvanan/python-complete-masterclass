# Chapter 36: Callback Functions

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:42:18

## Overview
A callback is a function passed as an argument to another function, which is called at a specific point (typically when an event occurs or a task completes).

## Common Use Cases
- Event handlers (button clicks, key presses)
- Async programming (on_success, on_error)
- Sorting with custom key functions
- Timer/schedule callbacks
- Observer pattern

## Callback Patterns
- Simple callback: pass function, call it once
- Error-first callback: callback(error, result)
- Event-based: register callback for event type

## Learning Outcomes
- Pass functions as callbacks
- Implement event systems with callbacks
- Use callbacks in sorting, filtering
- Handle async-style patterns