#!/usr/bin/env python3
"""return sum of provided list of float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of all the numbers in a list.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all the numbers in the list.
    """
    return sum(input_list)
