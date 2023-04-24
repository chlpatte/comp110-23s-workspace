"""File to define Bear class."""


class Bear:
    """Functions for the life cycle of the bears."""
    age: int
    hunger_score: int
     
    def __init__(self):
        """Initial values of the bear attributes."""
        self.age = 0
        self.hunger_score = 0
        return None
     
    def one_day(self):
        """How one day affects a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """The process of a bear eating."""
        self.hunger_score += num_fish
        return None
          