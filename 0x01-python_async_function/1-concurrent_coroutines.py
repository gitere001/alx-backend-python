#!/usr/bin/env python3
"""module containing wait_n coroutine."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n tasks that run wait_random coroutine with given max_delay.

    Args:
        n: The number of tasks to create.
        max_delay: The maximum delay for each task.

    Returns:
        List[float]: The delays of each task.
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    return [await task for task in asyncio.as_completed(tasks)]
