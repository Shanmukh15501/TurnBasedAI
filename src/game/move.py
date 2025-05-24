from game.cell import Cell

class Move:
    """
    Represents a move in the game, which consists of selecting a specific cell.
    """

    def __init__(self, cell: Cell):
        """
        Initializes a Move with the specified Cell.

        Args:
            cell (Cell): The cell associated with this move.
        """
        self._cell = cell

    def get_cell(self) -> Cell:
        """
        Retrieves the cell associated with this move.

        Returns:
            Cell: The cell where the move was made.
        """
        return self._cell
