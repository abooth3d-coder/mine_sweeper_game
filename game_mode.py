import sys
import config

timer: int = 0

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


def check_loose_condition(is_mine) -> None:
    if is_mine:
        print("You loose!\nGame Over!")
        print(f"Time on clock {(timer/60)} seconds.\n")
        sys.exit()


def add_second_to_timer() -> None:
    global timer
    timer += 1


class GameMode:
    def __init__(self):
        self.level = None
        self.difficulty: str = ""
        self.difficulty_selector()
        self.mines_left =0

    def found_mine_counter(self):
        self.mines_left -= 1

    def check_win_condition(self) -> None:
        if self.mines_left == 0:
            print(f"You won!\nYou found all {self.level['mines']} mines.")

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
                    self.mines_left = self.level["mines"]
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