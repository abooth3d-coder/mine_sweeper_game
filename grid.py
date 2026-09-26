import pygame

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

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def update(self) -> None:
        pass