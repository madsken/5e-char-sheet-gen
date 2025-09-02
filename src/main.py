from character import Character
from ch_class import Classes, CharacterClass
def main():
    char = Character("YESAE", CharacterClass(Classes.FIGHTER), "human", "soldier")
    print(char)


if __name__ == "__main__": 
    main()