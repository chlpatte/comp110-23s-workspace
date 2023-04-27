"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730580489"


class Simpy:
    """A simple version of NumPy."""

    values: list[float]
    
    def __init__(self, results: list[float]):
        """Initialize values to objects of class Point."""
        self.values = results
        return None

    def __repr__(self) -> str:
        """Print class name and values."""
        return f"Simpy({self.values})"
    
    def fill(self, input: float, num: int) -> None:
        """Fill Simpy with a set amount of a certain number."""
        result: list[float] = []
        for i in range(num):
            result.append(input)
        self.values = result
        return None
    
    def arange(self, begin: float, end: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        assert step != 0.0, "Step size cannot be zero."
        result: list[float] = []
        tracking: float = begin
        if begin < end:
            while tracking < end:
                result.append(tracking)
                tracking += step
        elif begin > end:
            while tracking > end:
                result.append(tracking)
                tracking += step
        else:
            raise ValueError("Begin and end values cannot be the same.")
        self.values = result
        return None
    
    def sum(self) -> float:
        """Return sum of all items in value attribute."""
        return sum(self.values)
    
    def __add__(self, right_side: Union[float, Simpy]) -> Simpy:
        """Make sure the right side of an addition problem is a SImpy or float."""
        result: Simpy = Simpy([])
        if isinstance(right_side, Simpy):
            assert len(self.values) == len(right_side.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + right_side.values[i])
        elif isinstance(right_side, float):
            for i in range(len(self.values)):
                result.values.append(self.values[i] + right_side)
        return result
    
    def __pow__(self, right_side: Union[float, Simpy]) -> Simpy: 
        """Allow one to use ** in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(right_side, float): 
            for i in range(len(self.values)): 
                result.values.append(self.values[i] ** right_side)
        elif isinstance(right_side, Simpy): 
            assert len(self.values) == len(right_side.values)
            i: int = 0
            while i < len(self.values): 
                result.values.append(self.values[i] ** right_side.values[i])
                i += 1
        return result

    def __eq__(self, right_side: Union[float, Simpy]) -> list[bool]: 
        """Make a mask based on equality of each item in values attribute with other values."""
        result: list[bool] = []
        if isinstance(right_side, float): 
            for i in range(len(self.values)): 
                if self.values[i] == right_side: 
                    result.append(True)
                else: 
                    result.append(False)
        elif isinstance(right_side, Simpy): 
            assert len(self.values) == len(right_side.values)
            for i in range(len(self.values)):
                if self.values[i] == right_side.values[i]: 
                    result.append(True)
                else: 
                    result.append(False)
        return result

    def __gt__(self, right_side: Union[float, Simpy]) -> list[bool]: 
        """Make a mask based on greater than relationship between item in value attribute with other values."""
        result: list[bool] = []
        if isinstance(right_side, float): 
            for i in range(len(self.values)): 
                if self.values[i] > right_side: 
                    result.append(True)
                else: 
                    result.append(False)
        elif isinstance(right_side, Simpy): 
            assert len(right_side.values) == len(right_side.values)
            for i in range(len(self.values)): 
                if self.values[i] > right_side.values[i]: 
                    result.append(True)
                else: 
                    result.append(False)
        return result

    def __getitem__(self, right_side: Union[int, list[bool]]) -> Union[float, Simpy]: 
        """Allow one to utilize subscription operator."""
        result: Simpy = Simpy([])
        if isinstance(right_side, int): 
            if right_side <= len(self.values): 
                return self.values[right_side]
        else:
            assert len(self.values) == len(right_side)
            for i in range(len(right_side)): 
                if right_side[i] is True: 
                    result.values.append(self.values[i])
        return result