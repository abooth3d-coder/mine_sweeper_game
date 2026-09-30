import grid
import cell
import constants
import random


def check_mine(cell_to_be_checked : cell.Cell) -> bool:
        if cell_to_be_checked.is_mine:
            return True
        return False


class MineGrid(grid.Grid):

    def __init__(self, width: int, height: int, cell_size: int):
        super().__init__(width, height, cell_size)
        self.populate_mines : int = constants.MINES_MAX


    def populating_mines(self):
        mined_cells = random.sample(self.cells, constants.MINES_MAX)
        for single_cell in mined_cells:
            single_cell.set_mine()
        self.populate_mines = 0