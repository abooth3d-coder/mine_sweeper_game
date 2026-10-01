import pygame
import constants
class Cell:
    pygame.font.init()
    CELL_FONT = pygame.font.SysFont("Arial", 22, bold=True)

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
        self.mine: str = "M"


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
        if self.is_mine:
            mine_text = self.CELL_FONT.render(self.mine, True, constants.MINE_COLOR)
            text_rect = mine_text.get_rect(center=rect.center)
            surface.blit(mine_text, text_rect)
        elif self.number > 0:
            # Map numbers directly to your existing constants
            color_map = {
                1: constants.ONE_COLOR,
                2: constants.TWO_COLOR,
                3: constants.THREE_COLOR,
                4: constants.FOUR_COLOR,
                5: constants.FIVE_COLOR,
                6: constants.SIX_COLOR,
                7: constants.SEVEN_COLOR,
                8: constants.EIGHT_COLOR
            }
            text_color = color_map.get(self.number, (0, 0, 0))

            number_text = self.CELL_FONT.render(str(self.number), True, text_color)
            text_rect = number_text.get_rect(center=rect.center)
            surface.blit(number_text, text_rect)