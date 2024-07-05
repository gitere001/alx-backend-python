#!/usr/bin/env python3
"""Module element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from `lst`
    and its length.

    Args:
    - lst (Iterable[Sequence]): Iterable containing sequences
    (e.g., lists, tuples).

    Returns:
    - List[Tuple[Sequence, int]]: List of tuples where each tuple contains an
    element from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
