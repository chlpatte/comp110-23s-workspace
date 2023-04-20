"""File to define River class"""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
    

    def bears_eating(self):
        for i in self.bears:
            if len(self.fish) > len(self.bears) * 3:
                Bear.eat(i, 3)
                self.remove_fish(3)   
        return None
    

    def check_hunger(self):
        new_bear_list: list = []
        for i in self.bears:
            if i.hunger_score > 0:
                new_bear_list.append(i)
        self.bears = new_bear_list
        return None


    def check_ages(self):
        new_bear_list: list = []
        for i in self.bears:
            if i.age < 6:
                new_bear_list.append(i)
        self.bears = new_bear_list
        new_fish_list: list = []
        for i in self.fish:
            if i.age < 4:
                new_fish_list.append(i)
        self.fish = new_fish_list
        return None
    

    def remove_fish(self, amount: int):
        new_fish_list: list = []
        num: int = 0
        for i in self.fish:
            num += 1
            if num > amount:
                new_fish_list.append(i)
        self.fish = new_fish_list
        return None

        
    def repopulate_fish(self):
        num: int = (len(self.fish) // 2) * 4
        if len(self.fish) < len(self.fish) + num:
            self.fish.append(Fish())
        return None
    

    def repopulate_bears(self):
        num: int = len(self.bears) // 2
        if len(self.bears) < len(self.bears) + num:
            self.bears.append(Bear())
        return None
    

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None


    def one_river_day(self):
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    

    def one_river_week(self):
        num: int = 0
        while num < 7:
            self.one_river_day()
            num += 1
        return None
