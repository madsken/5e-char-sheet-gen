from enum import Enum

class Stats(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

def match_stat(input_str):
    input_str = input_str.strip().lower()
    
    # Try matching by name
    for stat in Stats:
        if stat.name.lower() == input_str or stat.value.lower() == input_str:
            return stat
    return None