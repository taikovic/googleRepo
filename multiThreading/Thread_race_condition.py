#!/usr/bin/env python3
# Globa variable: counter is not protected any way; so no thread-safe
import concurrent.futures

counter = 0

def increment_counter(fake_value):
    global counter
    for _ in range(100):
        counter += 1
        print(counter)

if __name__ == "__main__":
    fake_data = [x for x in range(20)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(increment_counter,fake_data)
