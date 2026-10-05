import pygame
import config
import game_mode

class Cell:
    pygame.font.init()
    CELL_FONT = pygame.font.SysFont("Arial", 16, bold=False)

    def __init__(self, current_level: dict, current_game_mode ) -> None:
        self.current_level = current_level
        self.x: int = 0
        self.y: int = 0
        self.location: pygame.Vector2 = pygame.Vector2(0, 0)
        self.colour: pygame.Color = pygame.Color(config.BACKGROUND_COLOR)
        self.size: int = current_level["tile_size"]
        self.is_mine: bool = False
        self.number: int = 0
        self.flagged: bool = False
        self.is_revealed: bool = False
        self.mine: str = "M"
        self.current_game_mode = current_game_mode


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
        if self.flagged:
            flag_text = self.CELL_FONT.render("F", True, config.FLAG_COLOR)
            text_rect = flag_text.get_rect(center=rect.center)
            surface.blit(flag_text, text_rect)
            if self.is_mine:
                self.current_game_mode.found_mine()
                self.current_game_mode.check_win_condition()
        elif self.is_revealed:
            if self.is_mine:
                mine_text = self.CELL_FONT.render(self.mine, True, config.MINE_COLOR)
                text_rect = mine_text.get_rect(center=rect.center)
                surface.blit(mine_text, text_rect)
                game_mode.check_loose_condition(self.is_mine)
            elif self.number >= 0:
                # Map numbers directly to your existing constants
                color_map = {
                    0: config.ZERO_COLOR,
                    1: config.ONE_COLOR,
                    2: config.TWO_COLOR,
                    3: config.THREE_COLOR,
                    4: config.FOUR_COLOR,
                    5: config.FIVE_COLOR,
                    6: config.SIX_COLOR,
                    7: config.SEVEN_COLOR,
                    8: config.EIGHT_COLOR
                }
                text_color = color_map.get(self.number, (0, 0, 0))

                number_text = self.CELL_FONT.render(str(self.number), True, text_color)
                text_rect = number_text.get_rect(center=rect.center)
                surface.blit(number_text, text_rect)
                surface.blit(number_text, text_rect)