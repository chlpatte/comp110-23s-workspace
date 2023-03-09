"""Test for utils functions!"""

__author__ = "730580489"

from exercises.ex05.utils import only_evens, sub, concat


def test_odds() -> None:
    """Makes sure odds aren't added to the list!"""
    test_list: list[int] = [1, 3, 7]
    assert only_evens(test_list) == []


def test_evens() -> None:
    """Makes sure all evens are added to the list!"""
    test_list: list[int] = [2, 6, 8]
    assert only_evens(test_list) == [2, 6, 8]


def test_negatives() -> None:
    """Makes sure negatives works the same as positives!"""
    test_list: list[int] = [-2, -5, -7, -8]
    assert only_evens(test_list) == [-2, -8]


def test_order() -> None:
    """Makes sure the list maintain the order of the list!"""
    test_list1: list[int] = [1, 2, 3, 4]
    test_list2: list[int] = [5, 6, 7, 8]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_repetition() -> None:
    """Makes sure evey index is in he returned list even if it repeats!"""
    test_list1: list[int] = [1, 2, 2]
    test_list2: list[int] = [2, 2, 2]
    assert concat(test_list1, test_list2) == [1, 2, 2, 2, 2, 2]


def test_non_matching_len() -> None:
    """Makes sure you can combine lists that are not of the same length!"""
    test_list1: list[int] = [1, 2]
    test_list2: list[int] = [3, 4, 5, 6, 7]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6, 7]


def test_range_of_none() -> None:
    """Makes sure an empty list is returned if there is no given range!"""
    test_list: list[int] = [0, 1, 2]
    assert sub(test_list, 0, 0) == []


def test_range_out_of_index() -> None:
    """Makes sure a list is still returned if the range is longer or  lower than the list!"""
    test_list: list[int] = [0, 1, 2]
    assert sub(test_list, -1, 4) == [0, 1, 2]


def test_range_of_one() -> None:
    """Makes sure a list is returned given the smallest possible range!"""
    test_list: list[int] = [0, 1, 2]
    assert sub(test_list, 0, 1) == [0]