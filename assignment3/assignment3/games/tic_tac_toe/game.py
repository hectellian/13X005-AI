from assignment3.interfaces.game import IGame
from assignment3.games.tic_tac_toe.board import TicTacToeBoard

from typing import Tuple, Optional, List

class TicTacToeGame(IGame):
    """
    Class representing a Tic-Tac-Toe game.
    This class inherits from the AbstractGame class and implements its abstract methods.
    """

    def __init__(self):
        """
        Initialize the Tic-Tac-Toe game with an empty board and set the current player to 'X'.
        """
        self.board = TicTacToeBoard()
        self.current_player = 'X'

    def reset(self):
        """
        Reset the game to its initial state by creating a new empty board and setting the current player to 'X'.
        """
        self.board = TicTacToeBoard()
        self.current_player = 'X'

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
        if not self.board.place_move(x, y, self.current_player):
            return False, None  # Invalid move

        if self._check_win(x, y):
            return True, self.current_player

        if self.board.is_full():
            return True, 'Draw'

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return False, None

    def _check_win(self, x: int, y: int) -> bool:
        """
        Check if the current player has won by placing their move at (x, y).
        
        Parameters:
            x (int): Row index
            y (int): Column index
            
        Returns:
            bool: True if the player has won, False otherwise
        """
        # Check row, column, and diagonals
        return any([
            all(self.board.board[x][col] == self.current_player for col in range(3)),
            all(self.board.board[row][y] == self.current_player for row in range(3)),
            x == y and all(self.board.board[i][i] == self.current_player for i in range(3)),
            x + y == 2 and all(self.board.board[i][2 - i] == self.current_player for i in range(3))
        ])

    def render(self):
        """
        Render the current state of the game by displaying the Tic-Tac-Toe board.
        """
        self.board.display()
