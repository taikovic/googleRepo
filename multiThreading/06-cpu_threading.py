#!/usr/bin/env python3
# CPU-Bound problems; ex: arithmetic ops explosion
# Ce programme prendera plus de temps, pour executer le prg sequentiellement
# pas de overlap pdt une qlconque requeste des jobs des threads
# a ajouter le temps d'initialisation de threads
# tous les threads/tasks s'execute sur un seul cpu
import concurrent.futures
import time

def cpu_bound(number):
    return sum(i*i for i in range(number))

def find_sums(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound,numbers)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
