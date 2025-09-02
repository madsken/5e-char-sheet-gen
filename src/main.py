from typing import Dict
from character import Character
from ch_class import Classes, CharacterClass
from stats import Stats

from roll import roll_stats

def main():
    char = Character("YESAE", CharacterClass(Classes.FIGHTER), "human", "soldier")
    print(char)
    rolled_scores = roll_stats()
    print(rolled_scores)
    rolled_scores_dict = {
        Stats.STR: rolled_scores[0],
        Stats.DEX: rolled_scores[1],
        Stats.CON: rolled_scores[2],
        Stats.INT: rolled_scores[3],
        Stats.WIS: rolled_scores[4],
        Stats.CHA: rolled_scores[5]
    }
    char.set_ability_scores(rolled_scores_dict)
    print(char)


if __name__ == "__main__": 
    main()