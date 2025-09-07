import json
import os

class Race:
    def __init__(self, race_json):
        with open(race_json, 'r') as file:
            race_data = json.load(file)
        
        race_info  = race_data
        
        self.name = os.path.basename(race_json)[:-5].capitalize()
        self.ability_score_1 = race_info["ability_score_1"]
        self.ability_score_2 = race_info["ability_score_2"]
        self.size = race_info["size"]
        self.speed = race_info["speed"]
        self.languages = race_info["languages"]
        self.racial_feats = race_info["racial_feats"]


    def __repr__(self):
        return f"{self.name}"




    


