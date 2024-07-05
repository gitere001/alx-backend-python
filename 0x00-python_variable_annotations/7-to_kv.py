#!/usr/bin/env python3
"""a type-annotated function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple. The first element of the tuple is the
string k. The second element is the square of the int/float v and should be
annotated as a float"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string k, and the second
    element
    is the square of the input integer or float v. The second element is
    annotated
    as a float.

    Args:
        k (str): A string to be used as the first element of the tuple.
        v (int or float): An integer or float to be used as the second element
        of the tuple.

    Returns:
        Tuple[str, float]: A tuple with the first element being the string k
        and the second element being the square of the input v.

    """
    return (k, v**2)
