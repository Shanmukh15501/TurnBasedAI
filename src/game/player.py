class Player:
    """
    Represents a player in the game, identified by a unique symbol (e.g., 'X' or 'O').
    """

    def __init__(self, player_symbol: str):
        """
        Initializes a Player with the given symbol.

        Args:
            player_symbol (str): The symbol representing the player.
        """
        self._player_symbol = player_symbol

    def get_player_symbol(self) -> str:
        """
        Retrieves the player's symbol.

        Returns:
            str: The symbol associated with the player.
        """
        return self._player_symbol
