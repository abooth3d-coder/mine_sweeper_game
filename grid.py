import pygame
import cell

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

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def update(self) -> None:
        pass

    def create_cells(self) -> None:
        for row in range(0, self.height):
            for col in range(0, self.width):
                new_cell = cell.Cell(col, row)
                self.cells.append(new_cell)

    def create_grid(self) -> None:
        self.create_cells()
        grid_x: int = 0
        grid_y: int = 0
        for cell in self.cells:
            cell.set_x_y(grid_x, grid_y)
            if grid_x == 9:
                grid_x = 0
                grid_y += 1
            else:
                grid_x += 1

    def draw_grid(self, surface: pygame.Surface) -> None:
        for cell in self.cells:
            cell.draw_cell(surface)