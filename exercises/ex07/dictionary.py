"""Dictionary for ex07!"""

__author__ = "730580489"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    out_dict: dict[str, str] = dict()
    for i in inp_dict:
        out_dict[inp_dict[i]] = i
    raise KeyError("Keys in a dictionary must be unique, you cannot have two of the same.")