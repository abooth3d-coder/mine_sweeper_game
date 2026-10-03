import config

class GameMode:
    def __init__(self):
        self.difficulty : str = ""
        self.difficulty_selector()

    def difficulty_selector(self) -> None:
        is_valid : bool = False
        while not is_valid:
            print("Select a difficulty level:")
            for i, (difficulty, params) in enumerate(config.DIFFICULTY_LEVELS.items()):
                print(f"{i}. {difficulty}")
            difficulty = int(input("Choose a difficulty level: "))
            if 0 <= difficulty < len(config.DIFFICULTY_LEVELS):
                level = config.DIFFICULTY_LEVELS[difficulty]
                self.difficulty = level["difficulty"]
                is_valid = True
            else:
                print("Invalid choice. Please select a valid difficulty level.\n")
        print (f"You selected {self.difficulty} difficulty.")

GameMode()
