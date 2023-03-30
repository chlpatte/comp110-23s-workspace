"""Dictionary for ex07!"""

__author__ = "730580489"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Will make the keys the value and the value the keys."""
    tracking_list: list[str] = []
    for i in inp_dict:
        tracking_list.append(inp_dict[i])
    num: int = 1
    for i in tracking_list:
        if tracking_list.count(i) > num:
            raise KeyError("Keys in a dictionary are unique. This argument would return two of the same value.")
    out_dict: dict[str, str] = {}
    for i in inp_dict:
        out_dict[inp_dict[i]] = i
    return out_dict


def favorite_color(inp_dict: dict[str, str]) -> str:
    """Will count the most repeated value in a given dictionary and return it."""
    tracking_list: list[str] = []
    for i in inp_dict:
        tracking_list.append(inp_dict[i])
    idx: int = 0
    num: int = 0
    cur_max: int = 1
    for i in tracking_list:
        for x in tracking_list:
            if i == x:
                num += 1
        if num > cur_max:
            cur_max = num
            num = 0
            idx = tracking_list.index(i)
        else:
            num = 0
    return tracking_list[idx]


def count(inp_list: list[str]) -> dict[str, int]:
    """Counts the amount of times an element appears in a list and creates a dictionary with the element as the key and its quanity as its value."""
    out_dict: dict[str, int] = {}
    for i in inp_list:
        if i in out_dict:
            out_dict[i] = out_dict[i] + 1
        else:
            out_dict[i] = 1
    return out_dict