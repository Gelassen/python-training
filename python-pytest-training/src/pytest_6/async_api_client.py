# async_api_client.py

import aiohttp
import asyncio

async def async_fetch_data_from_api(url):
    """
    Asynchronously fetch data from the given URL using an HTTP GET request.

    :param url: URL of the API endpoint
    :return: Response object from the GET request
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"session {type(session)}")
            return await response.json()  # Assuming the response is in JSON format
