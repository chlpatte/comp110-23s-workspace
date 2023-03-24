"""Challenge Question 4!"""

__author__ = "730580489"

def zip(input: list[str], output: list[int]) -> dict[str, int]:
    chart: dict[str, int] = dict()
    if len(input) != len(output):
        return chart
    if len(input) == 0:
        return chart
    for i in range(0, len(input)):
        chart[input[i]] = output[i]
    return chart
