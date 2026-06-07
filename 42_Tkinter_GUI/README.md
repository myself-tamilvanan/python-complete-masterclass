# Chapter 42: Tkinter GUI

## Source
Based on: 12 Hours Python Masterclass in Tamil by Data Engineering (Gowtham)
Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:07:44

## Overview
Tkinter is Python's built-in GUI (Graphical User Interface) library. It allows you to create desktop applications with windows, buttons, labels, text fields, and more.

## Installation
Tkinter comes with Python. No installation needed!
```python
import tkinter as tk  # or: from tkinter import *
```

## Key Widgets
| Widget      | Description                    |
|-------------|--------------------------------|
| Tk()        | Main application window        |
| Label       | Display text or images         |
| Button      | Clickable button               |
| Entry       | Single-line text input         |
| Text        | Multi-line text input          |
| Frame       | Container for other widgets    |
| Canvas      | Drawing area                   |
| Listbox     | Scrollable list of items       |
| Combobox    | Dropdown selection (ttk)       |
| MessageBox  | Popup dialog boxes             |

## Layout Managers
| Manager | Description                           |
|---------|---------------------------------------|
| pack()  | Simple linear layout                  |
| grid()  | Table-like row/column layout          |
| place() | Absolute x,y positioning             |

## Learning Outcomes
- Create desktop GUI applications
- Use common Tkinter widgets
- Handle events with command callbacks
- Build a functional calculator or form