class Cell:
    """
    Represents a cell in a grid, identified by its row and column indices.
    """

    def __init__(self, row: int, col: int):
        """
        Initializes a new Cell with the specified row and column.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        self.row = row
        self.col = col

    def get_row(self) -> int:
        """
        Returns the row index of the cell.

        Returns:
            int: The row index.
        """
        return self.row

    def get_col(self) -> int:
        """
        Returns the column index of the cell.

        Returns:
            int: The column index.
        """
        return self.col
