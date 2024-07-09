#!/usr/bin/env python3
"""async_generator module"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    # Loop for 10 times
    for _ in range(10):
        # Wait for 1 second
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.random() * 10
