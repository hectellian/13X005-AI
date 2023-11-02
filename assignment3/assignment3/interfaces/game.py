from abc import ABC, abstractmethod

from typing import Tuple, Optional, List

class IGame(ABC):
    """
    Abstract class representing a generic game.
    This class defines the interface for all game-specific classes.
    """

    @abstractmethod
    def reset(self):
        """
        Reset the game to its initial state.
        """
        pass

    @abstractmethod
    def step(self, x: int, y: int) -> Tuple[bool, Optional[str]]:
        """
        Perform a game step by placing a move at the specified coordinates.

        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.

        Returns:
            tuple: A tuple containing:
                - game_over (bool): True if the game is over, False otherwise.
                - winner (str or None): The winner of the game, or None if the game is not over.
        """
        pass

    @abstractmethod
    def render(self):
        """
        Render the current state of the game, typically by displaying the game board.
        """
        pass
