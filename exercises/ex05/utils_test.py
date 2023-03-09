"""Test for utils functions!"""

__author__ = "730580489"

from exercises.ex05.utils import only_evens, sub, concat

def test_odds() -> None:
    test_list: list[int] = [1, 3, 7]
    assert only_evens(test_list) == []


def test_evens() -> None:
    test_list: list[int] = [2, 6, 8]
    assert only_evens(test_list) == [2, 6, 8]


#def test_() -> None:


def test_order() -> None:
    test_list1: list[int] = [1, 2, 3, 4]
    test_list2: list[int] = [5, 6, 7, 8]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_repetition() -> None:
    test_list1: list[int] = [1, 2, 2]
    test_list2: list[int] = [2, 2, 2]
    assert concat(test_list1, test_list2) == [1, 2, 2, 2, 2, 2]


#def test_


def test_range_of_none() -> None:
    test_list: list[int] = [0, 1, 2]
    assert sub(test_list, 0, 0) == []


def test_range_out_of_index() -> None:
    test_list: list[int] = [0, 1, 2]
    assert sub(test_list, -1, 4) == [0, 1, 2]


#def test_