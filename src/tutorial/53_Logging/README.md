# Chapter 53: Logging

## Overview
The logging module provides a flexible framework for emitting log messages. It is far superior to print() for tracking program behavior in production.

## Topics Covered
- Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Basic configuration with basicConfig()
- Logging to files
- Creating custom loggers
- Log formatting
- Handlers: StreamHandler, FileHandler
- Log rotation

## Key Concepts
- **Logger**: The object used to emit log messages
- **Handler**: Determines where log messages go (console, file)
- **Formatter**: Defines the format of log messages
- **Level**: Controls minimum severity to log
- **Root logger**: Default logger used by logging.info() etc.

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 2:20:10)

## Log Levels (lowest to highest)
| Level    | Value | Use case                          |
|----------|-------|-----------------------------------|
| DEBUG    | 10    | Detailed diagnostic info           |
| INFO     | 20    | Confirmation that things work      |
| WARNING  | 30    | Something unexpected (default min) |
| ERROR    | 40    | Serious problem                    |
| CRITICAL | 50    | Program may stop working           |

## Learning Outcomes
- Replace print() with appropriate logging
- Configure logging for files and console
- Create module-specific loggers
- Format log messages professionally
