import grid

class NumberGrid(grid.Grid):
    def __init__(self, width: int, height: int, cell_size: int):
        super().__init__(width, height, cell_size)