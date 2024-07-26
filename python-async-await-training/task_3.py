import asyncio
import aiofiles
from datetime import datetime

async def read_file(file_path):
    try:
        # Open the file in async mode
        async with aiofiles.open(file_path, mode='r') as file:
            # Read all lines from the file asynchronously
            lines = await file.readlines()
            # Process the lines (in this example, just printing them)
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

async def write_to_file(file_path, content):
    try:
        async with aiofiles.open(file_path, mode='w') as file:
            await file.write(content)
        print(f"Successfully wrote to file: {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

async def main():
    file_path = '/home/gelassen/Workspace/Sandbox/python-async-await-training/content/test_file.txt'
    content_to_write = f"time of writing to a file: {datetime.now()}"
    await read_file(file_path)
    await write_to_file(file_path, content_to_write)

if __name__ == "__main__":
    # Run the main coroutine in an event loop
    asyncio.run(main())
