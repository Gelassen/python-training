"""
    Parallel Execution:
    Write an async function that performs CPU-bound operations using 
    concurrent.futures.ProcessPoolExecutor or ThreadPoolExecutor with 
    await loop.run_in_executor().
"""
import asyncio
import concurrent.futures
import time
import os

# CPU-bound function
def cpu_bound_task(x):
    print(f"Processing {x} in process {os.getpid()}")
    time.sleep(2)  # Simulate a CPU-bound operation
    return x * x

async def main():
    loop = asyncio.get_running_loop()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        tasks = []
        for i in range(5):
            task = loop.run_in_executor(executor, cpu_bound_task, i)
            tasks.append(task)

    results = await asyncio.gather(*tasks)
    print(f"Results {results}")

asyncio.run(main())