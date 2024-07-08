#!/usr/bin/env python3
"""A module containing task_wait_random function."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create a task that runs the wait_random coroutine with given max_delay.

    Args:
        max_delay (int): The maximum delay for the task.

    Returns:
        asyncio.Task: The created task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
