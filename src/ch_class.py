
import json
from enum import Enum

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
    def __init__(self, class_enum):
        with open("../resources/classes.json", 'r') as file:
            classes_data = json.load(file)
        
        class_info = classes_data[class_enum.value]

        self.name = class_enum.value
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
        pass


if __name__=='__main__':
    char = CharacterClass(Classes.FIGHTER)
    print(char.primary_ability)
