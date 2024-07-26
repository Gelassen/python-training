"""
    Timeouts and Cancellation:
        Write an async function that performs a long-running task. 
        Use asyncio.wait_for() to set a timeout for this task. Handle the asyncio.TimeoutError exception.
"""

import asyncio

async def long_running_task():
    print("Task is started")
    try:
        await asyncio.sleep(5)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task was cancelled")    

async def main():
    try:
        await asyncio.wait_for(long_running_task(), timeout=2)
    except asyncio.TimeoutError:
        print("The task timed out!")

asyncio.run(main())