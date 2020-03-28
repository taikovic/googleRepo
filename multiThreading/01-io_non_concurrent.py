#!/usr/bin/env python3
#I/O bounding
# Synchronous way: easy and predictable;
import requests
import time



def download_site(url,session):
    with session.get(url) as response:
        #session.get() instead of requests.get() to spead UP
        #print(f"Read {len(response.content)} from {url}")
        pass
def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url,session)

if __name__ == "__main__":
    sites=["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")
