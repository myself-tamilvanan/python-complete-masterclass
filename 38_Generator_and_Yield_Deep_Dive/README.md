# Chapter 38: Generator & Yield (Deep Dive)

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:50:24

## Overview
Generators are memory-efficient iterators created using yield. This chapter goes deeper into generator features including yield from, send(), throw(), and generator pipelines.

## Key Features
- **yield**: Pauses function, returns value to caller, resumes on next()
- **yield from**: Delegate to another generator
- **send()**: Pass value back into the generator
- **throw()**: Raise exception inside generator
- **close()**: Terminate the generator

## Generator vs Iterator
| Generator           | Custom Iterator (class)     |
|---------------------|-----------------------------|
| Uses yield          | Needs __iter__ + __next__   |
| Less code           | More code                   |
| Auto StopIteration  | Manual StopIteration        |

## Use Cases
- Infinite sequences (IDs, timestamps)
- Processing large files line by line
- Data pipelines (ETL operations)
- Async-like patterns

## Learning Outcomes
- Use yield and yield from
- Send values to generators
- Build generator pipelines
- Create infinite generators