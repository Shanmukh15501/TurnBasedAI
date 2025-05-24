class GameResult:
    """
    Represents the result of a game, indicating whether the game is over and who the winner is.
    """

    def __init__(self, isOver: bool = False, winner: str = ""):
        """
        Initializes a new GameResult.

        Args:
            isOver (bool): True if the game is over; False otherwise.
            winner (str): The identifier/name of the winning player, if any.
        """
        self.isOver = isOver
        self.winner = winner

    def is_over(self) -> bool:
        """
        Checks whether the game is over.

        Returns:
            bool: True if the game is over; False otherwise.
        """
        return self.isOver

    def get_winner(self) -> str:
        """
        Gets the winner of the game.

        Returns:
            str: The name or symbol of the winning player, or an empty string if there is no winner.
        """
        return self.winner
