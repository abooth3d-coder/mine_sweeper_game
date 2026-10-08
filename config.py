#Profile constants
DIFFICULTY_LEVELS : dict = {
    "Easy": {"difficulty": "Easy", "grid_size": 9, "mines": 10, "tile_size": 35},
    "Medium": {"difficulty": "Medium", "grid_size": 16, "mines": 40, "tile_size": 30},
    "Hard": {"difficulty": "Hard", "grid_size": 24, "mines": 99,"tile_size": 25},
    "Extreme": {"difficulty": "Extreme", "grid_size": 30, "mines": 200,"tile_size": 20},
    "Insane": {"difficulty": "Insane", "grid_size": 40, "mines": 400, "tile_size": 15},
    #Custom difficulty allows the user to set their own grid size and number of mines (value 1 is a placeholder and will be replaced by user input)
    "Custom": {"difficulty": "Custom", "grid_size": 1, "mines": 1, "tile_size": 20}
}

#Colors
BACKGROUND_COLOR : tuple = (200, 200, 200)
MINE_COLOR : tuple = (0, 0, 0)
ZERO_COLOR : tuple = (255, 255, 255)
ONE_COLOR  : tuple = (0, 0, 255)
TWO_COLOR  : tuple = (0, 128, 0)
THREE_COLOR : tuple = (255, 0, 0)
FOUR_COLOR  : tuple = (128, 0, 128)
FIVE_COLOR : tuple = (255, 165, 0)
SIX_COLOR : tuple = (165, 42, 42)
SEVEN_COLOR : tuple = (255, 192, 203)
EIGHT_COLOR : tuple = (128, 128, 128)
FLAG_COLOR : tuple = (255, 100, 100)
