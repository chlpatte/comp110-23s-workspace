"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return sum of all elements"""
    sum_total: float = 0.0
    idx: int = 0
    for parts in range(0, len(xs)):
        sum_total += xs[idx]
        idx += 1
    return sum_total