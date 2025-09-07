import json
import os

class Background:
    def __init__(self, background_json):
        with open(background_json, 'r') as file:
            background_data = json.load(file)
        
        background_info  = background_data
        
        self.name = os.path.basename(background_json)[:-5].capitalize()
        self.skill_proficiencies = background_info["skill_proficiencies"]
        self.tool_proficiencies = background_info["tool_proficiencies"]
        self.languages = background_info["languages"]
        self.equipment = background_info["equipment"]
        self.features = background_info["features"]
    

    def __repr__(self):
        return f"{self.name}"
