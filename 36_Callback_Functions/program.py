# Chapter 36: Callback Functions
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 08:42:18
# ============================================

import time

print("--- Callback Functions ---")

# -----------------------------------------------
# SECTION 1: Basic Callback
# -----------------------------------------------

def fetch_data(callback):
    """Simulates fetching data and calling callback on completion."""
    print("  Fetching data...")
    time.sleep(0.1)  # Simulate work
    data = {"users": 10, "posts": 50}
    callback(data)   # Call the callback with result

def on_data_ready(data):
    print("  Data received:", data)

fetch_data(on_data_ready)
fetch_data(lambda d: print("  Lambda callback:", d["users"], "users"))

# -----------------------------------------------
# SECTION 2: Error-First Callbacks
# -----------------------------------------------

print("\n--- Error-First Callback ---")

def divide(a, b, callback):
    """Error-first pattern: callback(error, result)"""
    try:
        result = a / b
        callback(None, result)   # success: error=None
    except ZeroDivisionError as e:
        callback(str(e), None)   # failure: result=None

def handle_result(error, result):
    if error:
        print("  Error:", error)
    else:
        print("  Result:", result)

divide(10, 2, handle_result)
divide(10, 0, handle_result)

# -----------------------------------------------
# SECTION 3: Event System with Callbacks
# -----------------------------------------------

print("\n--- Event System ---")

class EventEmitter:
    """Simple event system using callbacks."""
    
    def __init__(self):
        self._listeners = {}
    
    def on(self, event, callback):
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)
    
    def emit(self, event, *args, **kwargs):
        for callback in self._listeners.get(event, []):
            callback(*args, **kwargs)

emitter = EventEmitter()

# Register callbacks
emitter.on("login", lambda u: print(f"  User logged in: {u}"))
emitter.on("login", lambda u: print(f"  Audit: Login recorded for {u}"))
emitter.on("logout", lambda u: print(f"  User logged out: {u}"))

# Trigger events
emitter.emit("login", "alice@example.com")
emitter.emit("logout", "alice@example.com")

# -----------------------------------------------
# SECTION 4: Sorting with Callbacks
# -----------------------------------------------

print("\n--- Callbacks in Built-ins ---")

people = [{"name":"Charlie","age":30},{"name":"Alice","age":25},{"name":"Bob","age":35}]

# sorted() uses callback as key function
by_name = sorted(people, key=lambda p: p["name"])
by_age = sorted(people, key=lambda p: p["age"])

print("By name:", [p["name"] for p in by_name])
print("By age:", [p["age"] for p in by_age])

print("\n" + "="*50)
print("Chapter 36 Complete!")
print("="*50)