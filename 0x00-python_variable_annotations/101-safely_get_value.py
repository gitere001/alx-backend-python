#!/usr/bin/env python3
"""module safely_get_value"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """
    Safely retrieves the value from a dictionary for a given key.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to retrieve the
        value.
        key (Any): The key for which to retrieve the value.
        default (Union[T, None], optional): The default value to return if the
        key is not found in the dictionary. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary, or
        the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
