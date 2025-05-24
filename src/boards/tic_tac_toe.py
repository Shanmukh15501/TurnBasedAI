import numpy as np
from game.board import Board
from game.cell import Cell

class TicTacToeBoard(Board):
    """
    Represents a Tic Tac Toe game board.
    This class manages the state of the Tic Tac Toe board, allowing for cell access and modification.
    Attributes:
        cells (np.ndarray): A 3x3 numpy array representing the Tic Tac Toe board.
        Methods:
            get_cell(row: int, col: int) -> str: Returns the value of the cell at the specified row and column.
            set_cell(value: str, cell: Cell): Sets the value of the specified cell to the given value.
    """
    
    def __init__(self):
        """
        Initializes a Tic Tac Toe board with a 3x3 grid filled with spaces.
        """
        self.cells = np.full((3, 3), " ")  # 3x3 board initialized with spaces
        
    def get_cell(self,row:int, col:int):
        """
        Returns the value of the cell at the specified row and column.
        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        Returns:
            str: The value of the cell at the specified position.
        """
        return self.cells[row][col]
    
    def set_cell(self,value:str,cell:Cell):
        """
        Sets the value of the specified cell to the given value.
        Args:
            value (str): The value to set in the cell (e.g., "X" or "O").
            cell (Cell): The cell object containing the row and column indices.
        """
        self.cells[cell.get_row()][cell.get_col()] = value
    
 