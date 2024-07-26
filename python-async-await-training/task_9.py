"""
    Web Scraping:
        Use aiohttp and BeautifulSoup to perform asynchronous web scraping of 
        multiple web pages concurrently.
"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup

# Function to fetch a single URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# Function to parse HTML content and extract the title
def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.title.string if soup.title else 'No title found'

# Function to fetch and parse a single URL
async def fetch_and_parse(session, url):
    html = await fetch(session, url)
    title = parse(html)
    print(f'Title: {title}')

# Main function to fetch multiple URLs concurrently
async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_and_parse(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

# List of URLs to scrape
urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.wikipedia.org',
]

# Run the main function
asyncio.run(main(urls))