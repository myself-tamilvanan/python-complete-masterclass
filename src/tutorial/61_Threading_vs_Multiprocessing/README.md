# Chapter 61: Threading vs Multiprocessing

## Overview
Python offers two main approaches for concurrent execution: threading and multiprocessing. Understanding the difference is crucial for writing efficient Python programs.

## Topics Covered
- Concurrency vs Parallelism
- The Global Interpreter Lock (GIL)
- I/O-bound vs CPU-bound tasks
- Threading: when to use it
- Multiprocessing: when to use it
- Performance comparison

## Key Concepts
- **GIL (Global Interpreter Lock)**: CPython limitation - only one thread executes Python bytecode at a time
- **I/O-bound**: Programs that spend most time waiting for I/O (files, network)
- **CPU-bound**: Programs that spend most time doing CPU computation
- **Thread**: Lightweight execution unit within a process (shares memory)
- **Process**: Independent execution unit with its own memory
- **Concurrency**: Multiple tasks in progress simultaneously
- **Parallelism**: Multiple tasks running at the exact same time

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 3:53:29)

## When to Use What
| Task Type  | Best Option      | Why                              |
|------------|------------------|----------------------------------|
| I/O-bound  | Threading        | GIL released during I/O waits    |
| CPU-bound  | Multiprocessing  | True parallelism across cores    |
| Simple     | asyncio          | Lightweight, single thread       |

## Learning Outcomes
- Understand the GIL and its implications
- Identify I/O-bound vs CPU-bound problems
- Choose the right concurrency model
