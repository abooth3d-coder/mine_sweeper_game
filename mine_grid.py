import grid
import cell
import config
import random
import pygame


def check_mine(cell_to_be_checked : cell.Cell) -> bool:
        if cell_to_be_checked.is_mine:
            return True
        return False


class MineGrid(grid.Grid):

    def __init__(self, width: int, height: int, cell_size: int):
        super().__init__(width, height, cell_size)
        self.populate_mines : int = config.MINES_MAX


    def populating_mines(self):
        mined_cells = random.sample(self.cells, config.MINES_MAX)
        for single_cell in mined_cells:
            single_cell.set_mine()
        self.populate_mines = 0

    def calculate_proximity_numbers(self):
        for target_cell in self.cells:
            if target_cell.is_mine:
                continue
            for offset_x in [-1, 0, 1]:
                for offset_y in [-1, 0, 1]:
                    if offset_x == 0 and offset_y == 0:
                        continue
                    neighbor_x = target_cell.x + offset_x
                    neighbor_y = target_cell.y + offset_y
                    if 0 <= neighbor_x < config.GRID_TILES and 0 <= neighbor_y < config.GRID_TILES:
                        for possible_neighbor in self.cells:
                            if possible_neighbor.x == neighbor_x and possible_neighbor.y == neighbor_y:
                                if possible_neighbor.is_mine:
                                    target_cell.add_number()


    def handle_click(self, mouse_pos: tuple[int, int], button_type: int) -> None:
        for single_cell in self.cells:
            cell_rect = pygame.Rect(
                single_cell.location.x * single_cell.size,
                single_cell.location.y * single_cell.size,
                single_cell.size,
                single_cell.size
            )
            if cell_rect.collidepoint(mouse_pos):
                if button_type == 1:  # Left-click
                    if not single_cell.is_revealed and not single_cell.flagged:
                        single_cell.reveal()
                elif button_type == 3:  # Right-click
                    if not single_cell.is_revealed:
                        single_cell.toggle_flagged()