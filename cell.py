import pygame
import constants
class Cell:

    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.location: pygame.Vector2 = pygame.Vector2(0, 0)
        self.colour: pygame.Color = pygame.Color(constants.BACKGROUND_COLOR)
        self.size: int = constants.GRID_SIZE
        self.is_mine: bool = False
        self.number: int = 0
        self.flagged: bool = False
        self.is_revealed: bool = False


    def set_mine(self) -> None:
        self.is_mine = True

    def set_x_y(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.location = pygame.Vector2(self.x, self.y)



    def add_number(self) -> None:
        self.number += 1

    def toggle_flagged(self) -> None:
        self.flagged = not self.flagged

    def reveal(self) -> None:
        self.is_revealed = True

    def draw_cell(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(self.location.x * self.size, self.location.y * self.size, self.size, self.size)
        pygame.draw.rect(surface, self.colour, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)