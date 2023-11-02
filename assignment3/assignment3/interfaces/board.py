from abc import ABC, abstractmethod

class IBoard(ABC):
    """
    Interface representing a generic game board. 
    This class defines the interface for all game-specific board classes.
    """

    @abstractmethod
    def place_move(self, x, y, symbol):
        """
        Place a move on the board.

        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
            symbol (str): The symbol to place ('X', 'O', etc.)

        Returns:
            bool: True if the move was placed successfully, False otherwise.
        """
        pass

    @abstractmethod
    def is_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        pass

    @abstractmethod
    def display(self):
        """
        Display the current state of the board.
        """
        pass
