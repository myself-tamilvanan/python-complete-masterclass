# Chapter 63: Multiprocessing
# Python Complete Masterclass
# Source: freeCodeCamp Intermediate Python by Patrick Loeber
# ============================================

import multiprocessing
import time
import os
from concurrent.futures import ProcessPoolExecutor

def square(n):
    result = n * n
    print(f"  Process {os.getpid()}: {n}^2 = {result}")
    return result

def cpu_heavy(n):
    return sum(i*i for i in range(n))

# IMPORTANT: multiprocessing requires this guard on Windows/macOS
if __name__ == "__main__":

    # -----------------------------------------------
    # SECTION 1: Creating Processes
    # -----------------------------------------------

    print("--- Creating Processes ---")

    p1 = multiprocessing.Process(target=square, args=(3,))
    p2 = multiprocessing.Process(target=square, args=(4,))
    p3 = multiprocessing.Process(target=square, args=(5,))

    p1.start(); p2.start(); p3.start()
    p1.join(); p2.join(); p3.join()

    print("All processes done")

    # -----------------------------------------------
    # SECTION 2: Process Pool
    # -----------------------------------------------

    print("\n--- Process Pool ---")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    # Pool.map - apply function to list in parallel
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print("Pool results:", results)

    # -----------------------------------------------
    # SECTION 3: ProcessPoolExecutor
    # -----------------------------------------------

    print("\n--- ProcessPoolExecutor ---")

    big_numbers = [10**6] * 4

    start = time.time()
    seq_results = [cpu_heavy(n) for n in big_numbers]
    seq_time = time.time() - start

    start = time.time()
    with ProcessPoolExecutor() as executor:
        par_results = list(executor.map(cpu_heavy, big_numbers))
    par_time = time.time() - start

    print(f"Sequential: {seq_time:.3f}s")
    print(f"Parallel:   {par_time:.3f}s")
    if par_time > 0:
        print(f"Speedup: {seq_time/par_time:.2f}x")

    # -----------------------------------------------
    # SECTION 4: Process Communication with Queue
    # -----------------------------------------------

    print("\n--- Queue Communication ---")

    def producer(queue, items):
        for item in items:
            queue.put(item)
            print(f"  Producer: sent {item}")
            time.sleep(0.1)
        queue.put(None)  # Sentinel to signal done

    def consumer(queue):
        while True:
            item = queue.get()
            if item is None:
                break
            print(f"  Consumer: received {item}")

    q = multiprocessing.Queue()

    p_prod = multiprocessing.Process(target=producer, args=(q, [1,2,3,4,5]))
    p_cons = multiprocessing.Process(target=consumer, args=(q,))

    p_prod.start(); p_cons.start()
    p_prod.join(); p_cons.join()

    # -----------------------------------------------
    # SECTION 5: Shared Memory
    # -----------------------------------------------

    print("\n--- Shared Memory ---")

    shared_val = multiprocessing.Value("i", 0)  # Shared integer
    lock = multiprocessing.Lock()

    def increment_shared(val, lock, times):
        for _ in range(times):
            with lock:
                val.value += 1

    processes = [
        multiprocessing.Process(target=increment_shared, args=(shared_val, lock, 100))
        for _ in range(4)
    ]

    for p in processes: p.start()
    for p in processes: p.join()

    print(f"Shared value (expected 400): {shared_val.value}")

    print("\n" + "="*50)
    print("Chapter 63 Complete!")
    print("Congratulations - Python Complete Masterclass Done!")
    print("="*50)
