from classes import Hero
from enter_dungeon import enter_dungeon_level_1

def get_hero_name():
    name = input("What is your name hero? ")
    return name

def get_hero_class():
    
    valid_classes = ["Wizard", "Barbarian", "Paladin"]
    while True: 
           hero_class = input(f"Choose your class ({', '.join(valid_classes)}): ").capitalize()
           if hero_class in valid_classes:
               return hero_class
           
           else:
               print(f"Invalid Class, Please choose from {', '.join(valid_classes)}.")

def start_game():

    hero_name = get_hero_name()
    hero_class = get_hero_class()
    
    hero = Hero(name=hero_name, hero_class=hero_class)
   
    if hero_class == "Wizard":
        valid_inventory_choice = ["Staff", "Pixie Dust", "Magical Brass Knuckles"]
        while True: 
            hero.add_to_inventory = input(f"Which of the following items would you like to start with? ({', '.join(valid_inventory_choice)}): ").capitalize()
            if hero.add_to_inventory in valid_inventory_choice:
                return hero.add_to_inventory
        
        else:
            print(f"You Greedy Mother blubber")

    print(f"Welcome, {hero_name} the {hero_class}!")
        
# Start the game loop or first event
enter_dungeon_level_1(Hero)

