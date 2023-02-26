"""Exercise Four!"""

__author__ = "730580489"


def all(array: list[int], num: int) -> bool:
    """Function determines if the given int matches all int in the given list."""
    matching: bool = True
    idx: int = 0
    while idx < len(array) and matching is True:
        if num == array[idx]:
            idx = idx + 1
        else:
            matching = False
    if matching is True:
        return True
    else:
        return False


def max(array: list[int]) -> int:
    """Function finds the largest/max int within the list provided."""
    if len(array) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    num: int = array[idx]
    while idx + 1 < len(array):
        if num > array[idx + 1]:
            idx = idx + 1
        else:
            num = array[idx + 1]
            idx = idx + 1
    return num


def is_equal(array1: list[int], array2: list[int]) -> bool:
    """Function determines if the list match eachother at every index."""
    if len(array1) != len(array2):
        return False
    idx: int = 0
    matching: bool = True
    while idx < len(array1) and matching is True:
        if array1[idx] == array2[idx]:
            idx = idx + 1
        else:
            matching = False
    if matching is True:
        return True
    else:
        return False