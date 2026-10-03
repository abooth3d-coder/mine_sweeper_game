import pygame
import cell
import config

class Grid(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, width: int, height: int, cell_size: int):
        # Check if containers are defined before unpacking them
        if hasattr(self, "containers") and self.containers:
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells : list[cell.Cell] = []


    def create_cells(self) -> None:
        for row in range(config.GRID_TILES):
            for col in range(config.GRID_TILES):
                new_cell = cell.Cell()
                new_cell.set_x_y(col, row)
                self.cells.append(new_cell)

    def create_grid(self) -> None:
        self.create_cells()


    def draw_grid(self, surface: pygame.Surface) -> None:
        for cell in self.cells:
            cell.draw_cell(surface)
