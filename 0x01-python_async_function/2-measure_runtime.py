#!/usr/bin/env python3

"""Module having measure_time function."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken by wait_n coroutine.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: The average time taken per task in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish_time = time.time()
    time_taken = finish_time - start_time
    return time_taken / n
