import pygame
import cell

class Grid(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, cell_size: int,active_level: dict, current_game_mode) -> None:
        super().__init__()
        self.width : int = width
        self.height : int = height
        self.cell_size : int = cell_size
        self.cells : list[cell.Cell] = []
        self.active_level : dict = active_level
        self.current_game_mode = current_game_mode


    def create_cells(self) -> None:
        for row in range(self.active_level["grid_size"]):
            for col in range(self.active_level["grid_size"]):
                new_cell = cell.Cell(self.active_level,self.current_game_mode)
                new_cell.set_x_y(col, row)
                self.cells.append(new_cell)

    def create_grid(self) -> None:
        self.create_cells()


    def draw_grid(self, surface: pygame.Surface) -> None:
        for cell in self.cells:
            cell.draw_cell(surface)
