#!/usr/bin/env python3
"""module 102-type_checking"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Generates a new list by repeating each element in the input list `lst` `
    factor` times.

    Parameters:
        lst (Tuple[Any, ...]): The input list to be zoomed in.
        factor (int, optional): The number of times each element should be
        repeated. Defaults to 2.

    Returns:
        List[Any]: The zoomed-in list.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Should be a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
