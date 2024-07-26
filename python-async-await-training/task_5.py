import asyncio
import random

"""
    Producer-Consumer:
        Implement a producer-consumer pattern using asyncio.Queue. The producer 
        should generate items and put them in the queue, while the consumer 
        takes items from the queue and processes them.
"""

async def producer(queue, n):
    for i in range(n):
        await asyncio.sleep(random.uniform(0.1, 0.5))
        item = f"item-{i}"
        await queue.put(item)
        print(f"Produced item: {item}")

    await queue.put(None)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            print("Consumer is stopped")
            break

        await asyncio.sleep(random.uniform(0.1, 0.5))
        print(f"consumed item {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    n = 10

    producer_task = asyncio.create_task(producer(queue, n))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task

    await queue.join()

    await consumer_task

    try: 
        await consumer_task
    except asyncio.CancelledError:
        pass

asyncio.run(main())