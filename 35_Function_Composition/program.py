# Chapter 35: Function Composition
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:39:57
# ============================================

from functools import reduce

print("--- Function Composition ---")

# Simple example: compose f and g => h(x) = f(g(x))
def double(x): return x * 2
def add_one(x): return x + 1
def square(x): return x * x

# Manual composition
def double_then_add(x):
    return add_one(double(x))

print("double then add_one (5):", double_then_add(5))   # 11

# compose() function
def compose(*funcs):
    """Compose functions right to left: compose(f, g)(x) = f(g(x))"""
    def composed(x):
        for func in reversed(funcs):
            x = func(x)
        return x
    return composed

# pipe() function (left to right - more natural for data pipelines)
def pipe(*funcs):
    """Pipe data through functions left to right."""
    def piped(x):
        for func in funcs:
            x = func(x)
        return x
    return piped

# Using compose
transform = compose(square, add_one, double)   # square(add_one(double(x)))
print("compose(square, add_one, double)(3):", transform(3))  # (3*2+1)^2 = 49

# Using pipe (more readable)
pipeline = pipe(double, add_one, square)   # x -> *2 -> +1 -> ^2
print("pipe(double, add_one, square)(3):", pipeline(3))   # (3*2+1)^2 = 49

# Data processing pipeline
text_pipeline = pipe(
    str.strip,
    str.lower,
    lambda s: s.replace(" ", "_"),
    lambda s: s.replace("@", "at")
)

 messy = "  Hello World! @ Home  "
print("Text pipeline:", text_pipeline("  Hello World! @ Home  "))

# Compose many functions
funcs = [str.strip, str.lower]
compose_all = lambda fs: reduce(lambda f, g: lambda x: g(f(x)), fs)
combined = compose_all(funcs)
print("Composed:", combined("  Hello World  "))

print("\n" + "="*50)
print("Chapter 35 Complete!")
print("="*50)