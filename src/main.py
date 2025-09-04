from typing import Dict
from character import Character
from ch_class import Classes, CharacterClass
from background import Background
from race import Race
from stats import Stats

from roll import roll_stats

def main():
    background = Background("resources/backgrounds/soldier.json")
    race = Race("resources/races/human.json")
    ch_class = CharacterClass("resources/classes/fighter.json")
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
    


if __name__ == "__main__": 
    main()