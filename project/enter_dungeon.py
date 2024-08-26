import random

def enter_dungeon_level_1(hero):
    valid_dungeons = ["Wine Cellar", "Jail Cell"]
    print(f"{hero.name} has entered the {random.choice(valid_dungeons)}!")