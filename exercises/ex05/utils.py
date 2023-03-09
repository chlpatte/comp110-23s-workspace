"""Practice testing functions!"""

__author__ = "730580489"

def only_evens(array: list[int]) -> list:
    idx: int = 0
    even_list: list[int] = list()
    for part in array:
        if array[idx] % 2 == 0:
            even_list.append(array[idx])
            idx += 1
        else:
            idx += 1
    return even_list


def concat(array1: list[int], array2: list[int]) -> list:
    new_list = list()
    for part in range(0, len(array1)):
        new_list.append(array1[part])
    for part in range(0, len(array2)):
        new_list.append(array2[part])
    return new_list


def sub(array: list[int], start: int, end: int) -> list:
    new_list = list()
    if len(array) == 0 or start >= len(array) or end <= 0:
        return new_list
    if start < 0:
        start = 0
    if end > len(array):
        end = len(array)
    for part in range(start, end):
        new_list.append(array[part])
    return new_list

