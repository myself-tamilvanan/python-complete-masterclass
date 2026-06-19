# Chapter 63: Multiprocessing

## Overview
Multiprocessing creates separate processes, each with their own Python interpreter and memory space, enabling true parallelism on multi-core CPUs.

## Topics Covered
- Process creation with multiprocessing.Process
- Process pools with Pool
- Process communication with Queue and Pipe
- Shared memory with Value and Array
- ProcessPoolExecutor
- Locks in multiprocessing

## Key Concepts
- **Process**: Independent execution unit with own memory space
- **Pool**: Managed collection of worker processes
- **Queue**: Thread/process-safe FIFO data structure for communication
- **Pipe**: Two-way communication channel between processes
- **Shared memory**: Value/Array for sharing data between processes

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 4:31:05)

## Process vs Thread
| Feature         | Process             | Thread              |
|-----------------|---------------------|---------------------|
| Memory          | Separate            | Shared              |
| GIL             | Not affected        | Affected            |
| Parallelism     | True (CPU-bound)    | Limited (GIL)       |
| Communication   | Queue/Pipe          | Shared vars + Lock  |
| Overhead        | Higher              | Lower               |

## Learning Outcomes
- Create and manage processes
- Use process pools for parallel computation
- Communicate between processes safely
- Share data between processes
