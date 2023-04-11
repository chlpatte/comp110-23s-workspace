"""Data Utility Functions!"""

__author__ = "730580489"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads CSV file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result 


def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Makes a new table with only the num amount of data."""
    result: dict[str, list[str]] = {}
    for key in table:
        collect: list[str] = []
        for i in table:
            collect.append(table(i))
        result[key] = collect
    return result