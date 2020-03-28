#!/usr/bin/env python3
# CPU-Bound problems; ex: arithmetic ops explosion
# diviser la charge sur les CPUs: 1 seul CPU charge / nombre de cpu (execution time)
#CPU-bound: use only mutliprocessing, No threads(threading), No tasks (asyncio)

import time
import multiprocessing

def cpu_bound(number):
    return sum(i*i for i in range(number))

def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound,numbers)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
