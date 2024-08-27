import random
import cast_spell from weapon_list

class Hero:
    
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory")
    
    def view_inventory(self):
        if self.inventory:
            print("Your inventory contains")
            for item in self.inventory:
                print(f"- {item}")
        
        else:
            print("Your Inventory is empty")


class Wizard:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 50
        self.inventory = []
        self.attacks = {
            "Fireball": (8,16),
            "Melee": (5),
        }



