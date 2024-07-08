#!/usr/bin/env python3
""" A module containing task_wait_n function. """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create n tasks that run task_wait_random with given max_delay.

    Args:
        n: The number of tasks to create.
        max_delay: The maximum delay for each task.

    Returns:
        List[float]: The delays of each task.
    """
    # Create a list of tasks by calling task_wait_random with max_delay
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to iterate over the tasks in the order
    # they complete. This is necessary because we want to return the
    # delays in the order they were created.
    return [await task for task in asyncio.as_completed(tasks)]
