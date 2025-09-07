from typing import Dict
from character import Character
from ch_class import Classes, CharacterClass
from background import Background
from race import Race
from stats import Stats, match_stat
import sys
import os
from rich import print

from roll import roll_stats


def print_main_menu(race, background, ch_class):
    print("")
    print(f"1: Choose race ([magenta]{race}[/magenta])")
    print(f"2: Choose background ([magenta]{background}[/magenta])")
    print(f"3: Choose class ([magenta]{ch_class}[/magenta])")
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
    
    if chosen_class.lower() in available_classes:
        return CharacterClass(f"resources/classes/{chosen_class.lower()}.json")
    else:
        return None


def make_character_sheet(race, background, ch_class):
    name = str(input("Please name your character:\n"))
    char = Character(name, ch_class, race, background)
    rolled_scores = roll_stats()
    rolled_scores_dict = assign_score_to_stat(rolled_scores)
    if rolled_scores_dict is None:
        print("[bold red]Error: Stat already chosen, stopping, please try again![/bold red]")
        return None
    char.set_ability_scores(rolled_scores_dict)
    char.chose_skill_proficiencies()
    return char

def assign_score_to_stat(rolled_scores):
    rolled_scores_dict = {}
    print(f"Rolled scores:\n{rolled_scores}")

    for score in rolled_scores:
        chosen_stat = str(input(f"Please chose stat to assign {score}\n"))
        chosen_stat = match_stat(chosen_stat)
        while chosen_stat is None:
            print("[yellow]Invalid stat, please chose again[/yellow]")
            chosen_stat = str(input(f"Please chose stat to assign {score}\n"))
            chosen_stat = match_stat(chosen_stat)
            
        if chosen_stat in rolled_scores_dict:
            return None
        else:
            rolled_scores_dict[chosen_stat] = score
    
    return rolled_scores_dict


def main():
    race = None
    background = None
    ch_class = None 
    while True:
        print_main_menu(race, background, ch_class)
        try:
            command = int(input("\nPlease choose your command: \n"))
        except ValueError:
            print("[bold red]Invalid input: Input number from 1-5[/bold red]")
            continue

        match command:
            case 1:
                race = chose_race()
                if race is not None:
                    print(f"Chosen race: {race.name}")
                else:
                    print("[bold red]Invalid race chosen[/bold red]")
            case 2:
                background = chose_background()
                if background is not None:
                    print(f"Chosen background: {background.name}")
                else:
                    print("[bold red]Invalid background chosen[/bold red]")
            case 3:
                ch_class = chose_class()
                if ch_class is not None:
                    print(f"Chosen class: {ch_class.name}")
                else:
                    print("[bold red]Invalid class chosen[/bold red]")
            case 4:
                if race == None or background == None or ch_class == None:
                    print("[bold red]ERROR: Have not chosen a race, background or class[/bold red]")
                else:
                    character = make_character_sheet(race, background, ch_class)
                    if character is None:
                        print("[bold red]Error in creating character[/bold red]")
                        continue
                    print("\nCharacter sheet done")
                    print("Character:")
                    print(character)
            case 5:
                print("Exiting...")
                sys.exit(0)
            case _:
                print("[bold red]Invalid input: Input number from 1-5[/bold red]")

    


if __name__ == "__main__": 
    main()