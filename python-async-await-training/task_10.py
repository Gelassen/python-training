"""
    Error Handling:
        Write an async function that includes proper error handling with try, 
        except, finally blocks to ensure resources are cleaned up properly 
        after an error occurs.
"""

import asyncio
import aiohttp

async def fetch(url):
    try:
        # Create an aiohttp ClientSession
        async with aiohttp.ClientSession() as session:
            # Perform an asynchronous GET request
            async with session.get(url) as response:
                # Check if the request was successful
                if response.status == 200:
                    # Return the response text
                    return await response.text()
                else:
                    # Raise an exception if the status code is not 200
                    raise aiohttp.ClientResponseError(
                        status=response.status,
                        message=f'Unexpected status code: {response.status}'
                    )
    except aiohttp.ClientError as e:
        # Handle any aiohttp client-related errors
        print(f'Client error occurred: {e}')
    except asyncio.TimeoutError:
        # Handle timeout errors
        print('Request timed out')
    except Exception as e:
        # Handle any other exceptions
        print(f'An error occurred: {e}')
    finally:
        # This block will be executed no matter what
        print('Cleanup actions can be performed here')

async def main():
    url = 'https://www.example.com'
    content = await fetch(url)
    if content:
        print(content)

# Run the main function
asyncio.run(main())
