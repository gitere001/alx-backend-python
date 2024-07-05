#!/usr/bin/env python3
"""a type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that creates and returns a function that multiplies a float by a
    given multiplier.

    Args:
    - multiplier (float): The multiplier to be used by the returned function.

    Returns:
    - Callable[[float], float]: A function that takes a float argument and
    returns the product of the argument and multiplier.
    """
    def multiplier_func(number: float) -> float:
        return number * multiplier

    return multiplier_func
