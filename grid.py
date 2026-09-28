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