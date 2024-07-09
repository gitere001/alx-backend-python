#!/usr/bin/env python3
"""measure_runtime module"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    An asynchronous function that measures the runtime of async_comprehension.

    Returns:
        float: The time taken to execute async_comprehension four times.
    """
    # Start the timer
    start = time.time()

    # Execute async_comprehension four times concurrently
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    # Stop the timer
    stop = time.time()

    # Return the time taken to execute async_comprehension four times
    return stop - start
