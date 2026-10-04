import config


def set_custom() -> dict:
    is_valid: bool = False
    custom_grid_size: int = 0
    mines: int = 0

    while not is_valid:
        try:
            custom_grid_size = int(input("Choose a grid size (e.g. 10 for a 10x10 grid): "))
            if custom_grid_size <= 0:
                print("Grid size must be greater than 0.\n")
                continue
            mines = int(input(f"Choose how many mines (must be less than {custom_grid_size * custom_grid_size}): "))
            if 0 < mines < (custom_grid_size * custom_grid_size):
                is_valid = True
            else:
                print(f"Invalid mine count. Mines must fit inside a {custom_grid_size}x{custom_grid_size} grid.\n")
        except ValueError:
            print("Please enter a valid whole number.\n")
    return {"grid_size": custom_grid_size, "mines": mines}


class GameMode:
    def __init__(self):
        self.level = None
        self.difficulty: str = ""
        self.difficulty_selector()

    def difficulty_selector(self) -> None:
        difficulty_keys = list(config.DIFFICULTY_LEVELS.keys())
        is_valid: bool = False
        while not is_valid:
            print("\nSelect a difficulty level:")
            for index, (difficulty, params) in enumerate(config.DIFFICULTY_LEVELS.items()):
                print(f"{index}. {difficulty}")
            try:
                choice = int(input("Choose a difficulty level: "))
                if 0 <= choice < len(difficulty_keys):
                    selected_difficulty = difficulty_keys[choice]

                    self.level = config.DIFFICULTY_LEVELS[selected_difficulty]
                    self.difficulty = selected_difficulty
                    is_valid = True
                else:
                    print("Invalid choice. Please select a number from the menu.\n")
            except ValueError:
                print("Please enter a valid numeric choice.\n")

        if self.difficulty == "Custom":
            self.level = set_custom()
        print(f"\nYou selected {self.difficulty} difficulty.")
        print(f"Active Parameters: {self.level}")

    def get_level(self):
        return self.level