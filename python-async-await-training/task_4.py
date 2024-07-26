"""
    HTTP Requests:
        Use aiohttp to make asynchronous HTTP GET requests to multiple URLs concurrently and print the status of each response.
"""

import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        print(f'URL: {url} | Status: {response.status}')
        print(f"Response as general: {response}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

# List of URLs to fetch
urls = [
    'https://www.example.com',
    'https://www.google.com',
    'https://www.python.org',
    'https://www.github.com'
]

# Running the main function
asyncio.run(main(urls))
