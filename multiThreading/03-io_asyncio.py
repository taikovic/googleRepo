#!/usr/bin/env python3
# using asyncio: pour operations asynchones s'executent sur un seul thread
# pour ne pas blocker le thread
# I/O bounding
import asyncio
import time
import aiohttp

# the function download_site() uses await;
# async: co-routine asynchrone;
async def download_site(session,url):
    async with session.get(url) as response:
        #print("Read {0} from {1}".format(response.content_length,url))
        pass

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session,url))
            tasks.append(task)
# blocker l'execution de la coroutine jusqu'a ce que cette instruction termine
        await asyncio.gather(*tasks,return_exceptions=False)

if __name__ == "__main__":
    sites=["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Download {len(sites)} in {duration} seconds")
