
import json
from enum import Enum
import os

#No bloodhunter, get rekt
class Classes(Enum):
    ARTIFICER = "Artificer"
    BARBARIAN = "Barbarian"
    BARD = "Bard"
    CLERIC = "Cleric"
    DRUID = "Druid"
    FIGHTER = "Fighter"
    MONK = "Monk"
    PALADIN = "Paladin"
    RANGER = "Ranger"
    ROGUE = "Rogue"
    SORCERER = "Sorcerer"
    WARLOCK = "Warlock"
    WIZARD = "Wizard"

class CharacterClass():
    def __init__(self, class_json):
        with open(class_json, 'r') as file:
            classes_data = json.load(file)
        
        class_info = classes_data

        self.name = os.path.basename(class_json)[:-5].capitalize()
        self.hit_die = class_info["hit_die"]
        self.primary_ability = class_info["primary_ability"]
        self.saving_throws = class_info["saving_throws"]
        self.armor_proficiencies = class_info["armor_proficiencies"]
        self.weapon_proficiencies = class_info["weapon_proficiencies"]
        self.tool_proficiencies = class_info["tool_proficiencies"]
        self.skill_choices = class_info["skill_choices"]
        self.starting_equipment = class_info["starting_equipment"]
        self.level_1_features = class_info["level_1_features"]

    def __repr__(self):
        print_str = ""
        print_str += f"Class: {self.name}\n\n"
        print_str += f"Hit die: d{self.hit_die}\n"
        print_str += f"Saving Throws: {self.saving_throws}\n"
        print_str += f"Armor proficiencies: {self.armor_proficiencies}\n"
        print_str += f"Weapon proficiencies: {self.weapon_proficiencies}\n"
        print_str += f"Tool proficiencies: {self.tool_proficiencies} \n"
        print_str += f"Skill choices: Chose {self.skill_choices['number_of_choices']} \n"
        print_str += f"{self.skill_choices["options"]}\n"        
        return print_str


if __name__=='__main__':
    char = CharacterClass(Classes.FIGHTER)
    print(char)
    char2 = CharacterClass(Classes.WIZARD)
    print(char2)