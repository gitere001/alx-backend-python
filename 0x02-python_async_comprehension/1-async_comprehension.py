#!/usr/bin/env python3
"""async_comprehension module"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An asynchronous comprehension that generates a list of random numbers
    between 0 and 10 from the async_generator.

    Returns:
        List[float]: A list of random numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
