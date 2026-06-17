# Chapter 62: Multithreading
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import threading
import time
from concurrent.futures import ThreadPoolExecutor

# -----------------------------------------------
# SECTION 1: Creating Threads
# -----------------------------------------------

print("--- Creating Threads ---")

def print_numbers(name, count, delay=0.1):
    for i in range(count):
        time.sleep(delay)
        print(f"  {name}: {i}")

# Create threads
t1 = threading.Thread(target=print_numbers, args=("Thread-1", 3))
t2 = threading.Thread(target=print_numbers, args=("Thread-2", 3))

t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print("Both threads done")

# -----------------------------------------------
# SECTION 2: Daemon Threads
# -----------------------------------------------

print("\n--- Daemon Threads ---")

def background_task():
    while True:
        print("  Background: still running...")
        time.sleep(0.5)

# Daemon threads automatically stop when main thread exits
t = threading.Thread(target=background_task)
t.daemon = True  # Mark as daemon
t.start()

print("Main thread: doing work...")
time.sleep(1.2)
print("Main thread: done (daemon will stop)")

# -----------------------------------------------
# SECTION 3: Race Conditions
# -----------------------------------------------

print("\n--- Race Conditions ---")

database_value = 0

def increment_without_lock(count):
    global database_value
    for _ in range(count):
        # Read - Modify - Write (not atomic!)
        local = database_value
        local += 1
        time.sleep(0.0001)   # Simulate small delay
        database_value = local

database_value = 0
t1 = threading.Thread(target=increment_without_lock, args=(10,))
t2 = threading.Thread(target=increment_without_lock, args=(10,))
t1.start(); t2.start()
t1.join(); t2.join()
print(f"Expected: 20, Got: {database_value} (race condition!)")

# -----------------------------------------------
# SECTION 4: Lock to Prevent Race Conditions
# -----------------------------------------------

print("\n--- Using Locks ---")

lock = threading.Lock()

def increment_with_lock(count):
    global database_value
    for _ in range(count):
        with lock:   # Acquire and release lock automatically
            local = database_value
            local += 1
            time.sleep(0.0001)
            database_value = local

database_value = 0
t1 = threading.Thread(target=increment_with_lock, args=(10,))
t2 = threading.Thread(target=increment_with_lock, args=(10,))
t1.start(); t2.start()
t1.join(); t2.join()
print(f"Expected: 20, Got: {database_value} (correct with lock!)")

# -----------------------------------------------
# SECTION 5: ThreadPoolExecutor
# -----------------------------------------------

print("\n--- ThreadPoolExecutor ---")

def download_page(url_num):
    time.sleep(0.2)  # Simulate network delay
    return f"Page {url_num} downloaded"

# Sequential
start = time.time()
results = [download_page(i) for i in range(5)]
seq_time = time.time() - start
print(f"Sequential: {seq_time:.2f}s")

# Thread pool
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(download_page, range(5)))
pool_time = time.time() - start
print(f"Thread pool: {pool_time:.2f}s")
print(f"Speedup: {seq_time/pool_time:.1f}x")

# submit() for individual futures
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_page, i) for i in range(3)]
    for future in futures:
        print("  Result:", future.result())

print("\n" + "="*50)
print("Chapter 62 Complete!")
print("="*50)
