#!/usr/bin/env python3
"""module for type checking"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Generates a new list by repeating each element in the input list `lst`
    `factor` times.

    Parameters:
        lst (Tuple): The input list to be zoomed in.
        factor (int, optional): The number of times each element should be
        repeated. Defaults to 2.

    Returns:
        List: The zoomed-in list with each element repeated `factor` times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
