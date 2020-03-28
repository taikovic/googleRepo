#!/usr/bin/env python3
# I/O bounding
# Thread using: OS is controlling the queue job of threads and their status: stop and continue running;
#That's Called: Tread swapping: pay attention to Data Access in this case;
# please refer to thread_race_condition.py script;

import requests
import time
import threading
import concurrent.futures
import os

#Separate access from different trades to different data, here using local strategy;
#use Threading.lock() if data shared

thread_local = threading.local()
# numCPU: here 4;
numCPU = os.cpu_count()
#max_workers: thread pool workers; 5-15
max_workers=15

def get_session():
    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        #session.get() instead of requests.get() to spead UP
        #print(f"Read {len(response.content)} from {url}")
        pass

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        executor.map(download_site,sites)

if __name__ == "__main__":
    sites=["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds for {max_workers} Threads")
