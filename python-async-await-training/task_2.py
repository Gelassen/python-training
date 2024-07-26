import os
import requests
import asyncio
import aiohttp

def list_files_and_folders(directory):
    items = []
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                items.append(entry.name)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {directory}.")
    return items

async def download_file(url, local_filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            with open(local_filename, 'wb') as file:
                while True:
                    chunk = await response.content.read(8192)
                    if not chunk:
                        break
                    file.write(chunk)
    print(f"File downloaded: {local_filename}")

async def run_scan_dir():
    # Example usage
    directory_path = '/home/gelassen/Workspace/Sandbox/python-async-await-training'  # Change to a more specific directory if needed
    items = list_files_and_folders(directory_path)
    print("Items in directory:", items)

async def run_downloading():
    # Example usage
    url = 'https://example-files.online-convert.com/raster%20image/png/example.png'
    local_filename = '/home/gelassen/Workspace/Sandbox/python-async-await-training/content/example.png'
    await download_file(url, local_filename)

async def main():
    await asyncio.gather(
        run_scan_dir(),
        run_downloading()
    )

asyncio.run(main())
