"Test for the dictionary functions for ex07!"

__author__ = "730580489"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_empty_dict() -> None:
    """Make sures when given an empty dictionary it returns an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_value_equals_key() -> None:
    """Makes sure the value can be the key as well."""
    test_dict: dict[str, str] = {"jordan": "jordan", "cole": "cole"}
    assert invert(test_dict) == {"jordan": "jordan", "cole": "cole"}


def test_length() -> None:
    """Makes sure the key and value are inverted no matter the length or lack there of."""
    test_dict: dict[str, str] = {"This should work": "", "": "I pray this works, I really need it to"}
    assert invert(test_dict) == {'': 'This should work', 'I pray this works, I really need it to': ''}


def test_only_one_color() -> None:
    """Makes sure the color is returned even if its the only color"""
    test_dict: dict[str, str] = {"k": "blue", "l": "blue", "m": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_earliest_color() -> None:
    """Makes sure the earliest color is returned if no other color is repeated more."""
    test_dict: dict[str, str] = {"1": "blue", "2": "blue", "3": "red", "4": "red"}
    assert favorite_color(test_dict) == "blue"


def test_only_values() -> None:
    """Makes sure only values are being counted towards the total."""
    test_dict: dict[str, str] = {"blue": "blue", "blue": "red", "blue": "red"}
    assert favorite_color(test_dict) == "red"


def test_empty_list() -> None:
    """Makes sure an empty list returns an empty dictionary."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_counts_whitespace_and_nospace() -> None:
    """Makes sure whitespaces and nospaces inside of quotation marks are counted and returned in a dictionary."""
    test_list: list[str] = ["", "", "", " ", " ", " ", " ", " ", " "]
    assert count(test_list) == {"": 3, " ": 6}


def test_capitalization() -> None:
    """Makes sure capitalization at any point in a string makes a difference."""
    test_list: list[str] = ["lee", "Lee", "lEe", "leE", "LeE", "lEE", "LEE", "lee", "lee", "LEE"]
    assert count(test_list) == {"lee": 3, "Lee": 1, "lEe": 1, "leE": 1, "LeE": 1, "lEE": 1, "LEE": 2}