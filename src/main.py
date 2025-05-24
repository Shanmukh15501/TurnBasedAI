
from api.GameEngine import GameEngine
from game.move import Cell, Move
from game.player import Player
    
class Main:
    """
    Main class to run the Tic Tac Toe game.
    This class initializes the game engine, sets up the players, and manages the game loop.
    It handles user input for moves and checks for game completion after each move.
    Attributes:
        game_engine (GameEngine): The game engine that manages the game logic.
        board (Board): The current state of the game board.
        computer (Player): The AI player.
        human (Player): The human player.   
    Methods:
        start(): Initializes the game and starts the game loop.
        __init__(): Constructor for the Main class.

    """
    def __init__(self):
        self.start()
    
    def start(self):
        game_init = input("Enter to start the game")
        game_init = game_init if game_init else "TicTacToe" # Default to TicTacToe
        self.game_engine = GameEngine()
        self.board = self.game_engine.start(game_init)
        self.computer = Player("X")
        self.human = Player("O")
        while(not self.game_engine.is_complete(self.board).is_over()):
            print("Enter your move (row and column): ")
            row = int(input("Row: "))
            col = int(input("Column: "))
            human_turn  = Move(Cell(row, col))
            self.game_engine.move(self.board, self.human, human_turn)
            print(self.board.cells)
            result = self.game_engine.is_complete(self.board)
            if  not result.is_over():
                print("AI is making a move...")
                ai_move = self.game_engine.suggest_ai_move(self.board)
                print(self.board.cells)
                if ai_move:
                    print("AI Move: ", ai_move)
                    self.game_engine.move(self.board, self.computer, ai_move)
                    print(self.board.cells)
            result = self.game_engine.is_complete(self.board)
            if result.is_over():
                print(f"Game Over!: Winner is {result.winner}")
                break

# Entry point equivalent to Java's main method
if __name__ == "__main__":
    main = Main()