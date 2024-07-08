#!/usr/bin/env python3
"""
Module containing wait_random function.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Return a random time delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The randomly generated delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
