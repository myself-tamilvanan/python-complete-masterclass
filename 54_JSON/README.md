# Chapter 54: JSON

## Overview
JSON (JavaScript Object Notation) is the most common data interchange format. Python's json module makes it easy to encode Python objects to JSON and decode JSON strings back to Python.

## Topics Covered
- json.dumps(): Python to JSON string
- json.loads(): JSON string to Python
- json.dump(): Write JSON to file
- json.load(): Read JSON from file
- Pretty printing with indent
- Custom encoding/decoding
- Handling non-serializable types

## Key Concepts
- **Serialization (encoding)**: Python object -> JSON string
- **Deserialization (decoding)**: JSON string -> Python object
- **JSON types**: object, array, string, number, boolean, null
- **indent**: Pretty-print JSON with indentation
- **sort_keys**: Sort dict keys alphabetically in output

## Source
- freeCodeCamp Intermediate Python by Patrick Loeber
- Video: https://youtu.be/HGOBQPFzWKo (Timestamp: 2:42:20)

## Python to JSON Type Mapping
| Python   | JSON    |
|----------|---------|
| dict     | object  |
| list     | array   |
| str      | string  |
| int/float| number  |
| True     | true    |
| False    | false   |
| None     | null    |

## Learning Outcomes
- Encode Python objects to JSON
- Decode JSON back to Python
- Read and write JSON files
- Handle special types with custom encoder
