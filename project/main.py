# main.py

import sys
import time
from starter_inputs import get_hero_name, get_hero_class, start_game
from starter_inputs import start_game


def typewriter(text, delay=0.05):
    """Function to print text like a typewriter effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_main_menu():
    """Function to display the main menu with ASCII art and choices."""
    # ASCII art for the game's title
    title_art = """
    
    
   ▄▄▄▄▀ ▄  █ ▄███▄       ▄███▄     ▄▄▄▄▀ ▄███▄   █▄▄▄▄   ▄   ██   █           ▄▀  ████▄ █     ██▄   
▀▀▀ █   █   █ █▀   ▀      █▀   ▀ ▀▀▀ █    █▀   ▀  █  ▄▀    █  █ █  █         ▄▀    █   █ █     █  █  
    █   ██▀▀█ ██▄▄        ██▄▄       █    ██▄▄    █▀▀▌ ██   █ █▄▄█ █         █ ▀▄  █   █ █     █   █ 
   █    █   █ █▄   ▄▀     █▄   ▄▀   █     █▄   ▄▀ █  █ █ █  █ █  █ ███▄      █   █ ▀████ ███▄  █  █  
  ▀        █  ▀███▀       ▀███▀    ▀      ▀███▀     █  █  █ █    █     ▀      ███            ▀ ███▀  
          ▀                                        ▀   █   ██   █                                    
                                                               ▀                                     

    """
    print(title_art)
    typewriter("Welcome to the Dungeon Adventure!\n")
    print("1. Play the Game")
    print("2. Credits")
    print("3. Exit")


def main():
    while True:
        display_main_menu()
        
        # Get the player's choice
        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == '1':
            # Start the game
            typewriter("\nStarting the game...\n")
            start_game()
            break  # Break out of the loop to start the game
        elif choice == '2':
            # Show credits
            typewriter("\nCredits:\n")
            typewriter("Game Developer: Kevin Petric\n")
            typewriter("Special Thanks: Oscar Sköld, David Hultén\n")
            input("\nPress Enter to return to the menu.")
        elif choice == '3':
            # Exit the game
            typewriter("\n Thank you, for playing the game!\n Exiting the game...\n")
            exit()
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
        

if __name__ == "__main__":
    
    main()
    
