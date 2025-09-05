from typing import Dict
from character import Character
from ch_class import Classes, CharacterClass
from background import Background
from race import Race
from stats import Stats
import sys
import os

from roll import roll_stats


def print_main_menu():
    print("")
    print("1: Choose race")
    print("2: Choose background")
    print("3: Choose class")
    print("4: Generate character sheet")
    print("5: Exit")


def get_items_in_folder(folder):
    target_dir = os.path.join(os.path.abspath("resources"), folder)
    items = os.listdir(target_dir)
    for item in items:
        print(item[:-5].capitalize())
    return [os.path.splitext(f)[0] for f in items]

def chose_race():
    print("\nAvailable races:")
    available_races = get_items_in_folder("races")
    chosen_race = str(input("Please chose a race:\n"))

    if chosen_race.lower() in available_races:
        return Race(f"resources/races/{chosen_race.lower()}.json")
    else:
        return None

def chose_background():
    print("\nAvailable backgrounds:")
    available_backgrounds = get_items_in_folder("backgrounds")
    chosen_background = str(input("Please chose a background:\n"))

    if chosen_background.lower() in available_backgrounds:
        return Background(f"resources/backgrounds/{chosen_background.lower()}.json")
    else:
        return None

def chose_class():
    print("\nAvailable classes:")
    available_classes = get_items_in_folder("classes")
    chosen_class = str(input("Please chose a class:\n"))
    
    print(available_classes)
    print(f"\n\nis chosen class in available: {chosen_class in available_classes}")

    if chosen_class.lower() in available_classes:
        return CharacterClass(f"resources/classes/{chosen_class.lower()}.json")
    else:
        return None


def make_character_sheet(race, background, ch_class):
    # print(ch_class)
    char = Character("YESAE", ch_class, race, background)
    rolled_scores = roll_stats()
    rolled_scores_dict = {
        Stats.STR: rolled_scores[0],
        Stats.DEX: rolled_scores[1],
        Stats.CON: rolled_scores[2],
        Stats.INT: rolled_scores[3],
        Stats.WIS: rolled_scores[4],
        Stats.CHA: rolled_scores[5]
    }
    char.set_ability_scores(rolled_scores_dict)
    char.chose_skill_proficiencies()
    return char


def main():
    race = None
    background = None
    ch_class = None 
    while True:
        print_main_menu()
        command = int(input("\nPlease choose your command: \n"))
        match command:
            case 1:
                race = chose_race()
                if race is not None:
                    print(f"Chose race: {race.name}")
                else:
                    print("Invalid race chose")
            case 2:
                background = chose_background()
                if background is not None:
                    print(f"Chose background: {background.name}")
                else:
                    print("Invalid background chosen")
            case 3:
                ch_class = chose_class()
                if ch_class is not None:
                    print(f"Chose class: {ch_class.name}")
                else:
                    print("Invalid class chosen")
            case 4:
                if race == None or background == None or ch_class == None:
                    print("Have not chosen a race, background or class")
                else:
                    character = make_character_sheet(race, background, ch_class)
                    print("\nCharacter sheet done")
                    print("Character:")
                    print(character)
            case 5:
                print("Exiting...")
                sys.exit(0)

    


if __name__ == "__main__": 
    main()