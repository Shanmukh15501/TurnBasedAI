from game.gameresult import GameResult
from game.player import Player
from game.board import Board
from boards.tic_tac_toe import TicTacToeBoard
from game.move import Cell, Move
import numpy as np

class GameEngine:
    """
    GameEngine class to manage the game logic and flow.
    This class is responsible for starting the game, making moves, checking for game completion,
    and suggesting AI moves.
    Attributes:
        None
    Methods:
        start(game_type: str) -> Board: Initializes the game board based on the game type.
        move(board: Board, player: Player, move: Move): Makes a move on the board for the given player.
        is_complete(board: Board) -> GameResult: Checks if the game is complete and returns the result.
        suggest_ai_move(board: Board) -> Move: Suggests a move for the AI player.
    """
    def __init__(self):
        pass
    def start(self, game_type: str) -> Board:
        """
        Initializes the game board based on the game type.
        Args:
            game_type (str): The type of game to start (e.g., "TicTacToe").
        Returns:
            Board: The initialized game board.
        """
            
        if game_type == "TicTacToe":
            return TicTacToeBoard()
        else:
            raise ValueError("Unsupported game type")

    def move(self, board: Board,player: Player,move: Move):
        """
        Makes a move on the board for the given player.
        Args:
            board (Board): The game board.
            player (Player): The player making the move.
            move (Move): The move to be made.
        """
        if isinstance(board, TicTacToeBoard):
            board.set_cell(player.get_player_symbol(),move.get_cell())
        else:
            raise ValueError("Unsupported board type")

    def is_complete(self,board: Board):
        """
        Checks if the game is complete and returns the result.
        Args:
            board (Board): The game board.
        Returns:        
            GameResult: The result of the game (e.g., winner, draw).
        """

        if isinstance(board, TicTacToeBoard):
            try:
                row_complete = False
                col_complete = False
                diag_complete = False
                rev_diag_complete = False
                for i in range(3):
                    first_char = board.get_cell(i,0)
                    
                    for j in range(3):
                        if board.cells[i][j] == first_char and first_char != " ":
                            row_complete = True
                        else:
                            row_complete = False                            
                            break
                    if row_complete:
                        return GameResult(True, first_char)
               
                for i in range(3):
                    first_char = board.get_cell(0,i)
                    for j in range(3):
                        if board.cells[j][i] == first_char and first_char != " ":
                            col_complete = True
                        else:
                            col_complete = False
                            break
                    if col_complete:
                        return GameResult(True, first_char)
                
                first_char = board.get_cell(0,0)
                
                for i in range(3):
                    if board.cells[i][i] == first_char and first_char != " ":
                        diag_complete = True
                    else:
                        diag_complete = False
                        break
                    
                if diag_complete:
                    return GameResult(True, first_char)
                
                first_char = board.get_cell(0,2)                
                for i in range(3):
                    if board.cells[i][2 - i] == first_char and first_char != " ":
                        rev_diag_complete = True
                    else:
                        rev_diag_complete = False
                        break
                
                if rev_diag_complete:
                    return GameResult(True, first_char)
                
                if np.count_nonzero(board.cells == ' ') == 0:
                    print("-----Draw-----------")
                    return GameResult(True, "-")
                return GameResult(False, "-")
            except Exception as e:
                print(f"Error in is_complete: {e}")
                return GameResult(False, "-")
       
    def suggest_ai_move(self, board: Board) -> Move:
        """
        Suggests a move for the AI player.
        Args:
            board (Board): The game board.
        Returns:
            Move: The suggested move for the AI player.
        """
        if isinstance(board, TicTacToeBoard):
            for i in range(3):
                for j in range(3):
                    if board.cells[i][j] == " ":
                        return Move(Cell(i, j))
        return None    