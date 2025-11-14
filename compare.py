# Empirical comparison of deterministic vs randomized Quicksort

import time
import random
import sys

# Increase recursion limit for large arrays
sys.setrecursionlimit(30000)

# Import your implementations
from quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def run_test(sort_func, arr):
    start = time.time()
    sort_func(arr, 0, len(arr)-1)
    return time.time() - start

def generate_inputs(n):
    """Generate three types of arrays: random, sorted, reverse-sorted"""
    return {
        "random": [random.randint(1, 100000) for _ in range(n)],
        "sorted": list(range(n)),
        "reverse": list(range(n, 0, -1))
    }

sizes = [5000, 10000, 20000]

for n in sizes:
    print(f"\n====== n = {n} ======")
    inputs = generate_inputs(n)

    for dist, arr in inputs.items():
        arr1 = arr.copy()   # deterministic test
        arr2 = arr.copy()   # randomized test

        t1 = run_test(quicksort, arr1)
        t2 = run_test(randomized_quicksort, arr2)

        print(f"{dist} input:")
        print(f"  Deterministic: {t1:.5f} sec")
        print(f"  Randomized:    {t2:.5f} sec")
