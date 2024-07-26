from datetime import datetime
import asyncio

async def run_and_sleep():
    while True:
        current_datetime = datetime.now()
        print("Current date and time:", current_datetime)
        await asyncio.sleep(3)

asyncio.run(run_and_sleep())