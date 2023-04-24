"""File to define Fish class."""


class Fish:
    """Functions for the life cycle of fish."""
    age: int
    
    def __init__(self):
        """Initial value of the fish attributes."""
        self.age = 0
        return None
    
    def one_day(self):
        """How one day affects the fish."""
        self.age += 1
        return None