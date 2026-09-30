import pygame
import cell
import constants

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
        for row in range(constants.GRID_TILES):
            for col in range(constants.GRID_TILES):
                new_cell = cell.Cell()
                new_cell.set_x_y(col, row)
                self.cells.append(new_cell)

    def create_grid(self) -> None:
        self.create_cells()


    def draw_grid(self, surface: pygame.Surface) -> None:
        for cell in self.cells:
            cell.draw_cell(surface)

    def draw_cell(self, surface: pygame.Surface) -> None:
        # 1. Calculate the base pixel coordinates, then add a 10-pixel offset
        pixel_x = (self.location.x * self.size) + 10
        pixel_y = (self.location.y * self.size) + 10

        # 2. Use those shifted coordinates to create your rectangle
        rect = pygame.Rect(pixel_x, pixel_y, self.size, self.size)

        # 3. Draw the background and the border
        pygame.draw.rect(surface, self.colour, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)
