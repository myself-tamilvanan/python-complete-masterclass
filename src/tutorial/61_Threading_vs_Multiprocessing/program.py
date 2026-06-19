# Chapter 61: Threading vs Multiprocessing
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import multiprocessing
import threading
import time

# -----------------------------------------------
# SECTION 1: Sequential Execution (baseline)
# -----------------------------------------------

print("--- Sequential Execution ---")


def cpu_task(name, n):
    total = 0
    for i in range(n):
        total += i
    return total


def io_task(name, duration):
    time.sleep(duration)  # Simulates I/O wait
    print(f"  {name} completed after {duration}s")


# Run I/O tasks sequentially
start = time.time()
io_task("Task-1", 0.5)
io_task("Task-2", 0.5)
io_task("Task-3", 0.5)
print(f"Sequential I/O time: {time.time() - start:.2f}s")

# -----------------------------------------------
# SECTION 2: Threading for I/O-bound
# -----------------------------------------------

print("\n--- Threading for I/O-bound ---")

# GIL is RELEASED during I/O operations - so threads help
start = time.time()

threads = []
for i in range(3):
    t = threading.Thread(target=io_task, args=(f"Thread-{i + 1}", 0.5))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Threaded I/O time: {time.time() - start:.2f}s")

# -----------------------------------------------
# SECTION 3: CPU-bound Comparison
# -----------------------------------------------

print("\n--- CPU-bound Comparison ---")


def count(n=5000000):
    return sum(range(n))


# Sequential
start = time.time()
count()
count()
seq_time = time.time() - start
print(f"Sequential: {seq_time:.3f}s")

# Threaded (GIL limits CPU parallelism)
start = time.time()
t1 = threading.Thread(target=count)
t2 = threading.Thread(target=count)
t1.start()
t2.start()
t1.join()
t2.join()
thread_time = time.time() - start
print(f"Threaded: {thread_time:.3f}s (similar or slower due to GIL)")

# Multiprocessing (true parallelism)
if __name__ == "__main__":
    start = time.time()
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    mp_time = time.time() - start
    print(f"Multiprocessing: {mp_time:.3f}s (faster with multiple cores)")

# -----------------------------------------------
# SECTION 4: The GIL Explained
# -----------------------------------------------

print("\n--- The GIL ---")

print("Global Interpreter Lock (GIL):")
print("- CPython allows only ONE thread to execute Python at a time")
print("- GIL is RELEASED during I/O operations (file, network, sleep)")
print("- For CPU-bound tasks: use multiprocessing (separate GIL per process)")
print("- For I/O-bound tasks: use threading or asyncio")

# -----------------------------------------------
# SECTION 5: Decision Guide
# -----------------------------------------------

print("\n--- Decision Guide ---")


def is_io_bound(task_description):
    io_keywords = ["download", "upload", "file", "database", "network", "api", "sleep", "wait"]
    return any(kw in task_description.lower() for kw in io_keywords)


tasks = [
    "Download 100 images",
    "Calculate prime numbers",
    "Read data from database",
    "Compress 10GB of video",
    "Send 1000 API requests",
]

print("Task -> Recommended approach:")
for task in tasks:
    if is_io_bound(task):
        print(f"  {task}: -> threading or asyncio")
    else:
        print(f"  {task}: -> multiprocessing")

print("\n" + "=" * 50)
print("Chapter 61 Complete!")
print("=" * 50)
