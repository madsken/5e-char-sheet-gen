from typing import List, Dict
from skills import Skills
from stats import Stats
from ch_class import CharacterClass, Classes
from race import Race
from background import Background


class Character():
    def __init__(self, name, ch_class, race, background, level=1, alignment="Neutral", exp=0):
        self.name = name
        self.ch_class = ch_class
        self.race = race
        self.background = background
        self.level = level
        self.alignment = alignment
        self.exp = exp

        self.ability_scores = {
            Stats.STR: 10,
            Stats.DEX: 10,
            Stats.CON: 10,
            Stats.INT: 10,
            Stats.WIS: 10,
            Stats.CHA: 10,
        }

        # Skills will be populated from class, background, etc.
        self.skill_proficiencies: List[Skills] = []
        self.skill_proficiencies.extend(background.skill_proficiencies)
        self.saving_throw_proficiencies = self.ch_class.saving_throws

        self.hp = self.calc_level1_hp()
        self.hit_dice_type = self.ch_class.hit_die
        self.hit_dice_max = self.level

        self.proficiencies = self.collect_proficiencies()
        self.features = self.ch_class.level_1_features

    def calc_level1_hp(self):
        con_score = self.ability_scores[Stats.CON]
        con_mod = self.get_modifier(con_score)
        return self.ch_class.hit_die + con_mod

    def get_modifier(self, score):
        return (score - 10) // 2
    
    def collect_proficiencies(self):
        tool_prof = self.ch_class.tool_proficiencies + self.background.tool_proficiencies
        return {
            "Armor": self.ch_class.armor_proficiencies,
            "Weapons": self.ch_class.weapon_proficiencies,
            "Tools": self.ch_class.tool_proficiencies
        }

    def set_ability_scores(self, scores: Dict[Stats, int]):
        for stat, value in scores.items():
            if stat in self.ability_scores:
                self.ability_scores[stat] = value
                if stat.value in self.race.ability_score_1:
                    self.ability_scores[stat] += 1
                if stat.value in self.race.ability_score_2:
                    self.ability_scores[stat] += 2
        self.hp = self.calc_level1_hp()

    def add_skill_proficiencies(self, skills: List[Skills]):
        self.skill_proficiencies.extend(skills)

    def chose_skill_proficiencies(self):
        count = self.ch_class.skill_choices['number_of_choices']
        while count > 0:
            print("\nCurrent skill proficiencies:")
            for skill in self.skill_proficiencies:
                print(skill)
            print("")
            print("Available skill to chose from:")
            for skill in self.ch_class.skill_choices["options"]:
                print(skill)
            print("")
            chosen_skill = input(f"Please chose a skill to become proficient in ({count} left): \n")

            if chosen_skill.capitalize() in self.skill_proficiencies:
                print("ERROR: Skill is already proficient. Chose another.")
                continue
        
            self.skill_proficiencies.append(chosen_skill.capitalize())
            count -= 1
        print("===Final Skills===")
        print(self.skill_proficiencies)

    def __str__(self):
        print_str = f"{self.name}, Level {self.level} {self.ch_class.name} ({self.race})\n\n"
        print_str += f"Ability scores:\n"
        for stat, score in self.ability_scores.items():
            print_str += f"{stat.value} : {score}\n"
        
        print_str += f"HP: {self.hp}\n"
        print_str += f"Hit dice: {self.hit_dice_max}d{self.hit_dice_type}\n\n"

        print_str += f"Skill proficiencies: {self.skill_proficiencies}\n\n"
        print_str += f"Saving throw proficiencies: {self.saving_throw_proficiencies}\n\n"


        return print_str


if __name__=='__main__':
    test = Character("test", CharacterClass(Classes.FIGHTER), "Human", "Soldier")
    print(test.ability_scores)





