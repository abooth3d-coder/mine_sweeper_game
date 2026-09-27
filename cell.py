import pygame
import constants
class Cell:


    def __init__(self, x : int,y : int) -> None:
        self.location : pygame.Vector2 = pygame.Vector2(x,y)
        self.colour : pygame.Color = pygame.Color(constants.BACKGROUND_COLOR)
        self.size : int = constants.GRID_SIZE
        self.is_mine: bool = False
        self.number: int = 0
        self.flagged: bool = False


    def set_mine(self) -> None:
        self.is_mine = True


    def add_number(self) -> None:
        self.number += 1

    def toggle_flagged(self) -> None:
        self.flagged = not self.flagged