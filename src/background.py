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
        print_str = ""
        print_str += f"background name: {self.name}\n\n"
        print_str += f"skill prof: {self.skill_proficiencies}\n"
        print_str += f"tool prof: {self.tool_proficiencies}\n"
        print_str += f"language: {self.languages}\n"
        print_str += f"equipment: {self.equipment}\n"
        print_str += f"features: {self.features} \n"
        return print_str
