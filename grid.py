import pygame
import cell
import config

class Grid(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, width: int, height: int, cell_size: int,active_level: dict) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells : list[cell.Cell] = []
        self.active_level = active_level


    def create_cells(self) -> None:
        for row in range(self.active_level["grid_size"]):
            for col in range(self.active_level["grid_size"]):
                new_cell = cell.Cell(self.active_level)
                new_cell.set_x_y(col, row)
                self.cells.append(new_cell)

    def create_grid(self) -> None:
        self.create_cells()


    def draw_grid(self, surface: pygame.Surface) -> None:
        for cell in self.cells:
            cell.draw_cell(surface)
