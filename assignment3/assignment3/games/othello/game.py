from assignment3.interfaces.game import IGame
from assignment3.games.othello.board import OthelloBoard

class OthelloGame(IGame):
    """
    Class representing an Othello game.
    This class inherits from the IGame class and implements its abstract methods.
    """

    def __init__(self):
        """
        Initialize the Othello game with an empty board.
        """
        self.board = OthelloBoard()
        self.current_player = '○' # Black player starts first
        
    def switch_player(self):
        """
        Switch the current player.
        """
        self.current_player = '●' if self.current_player == '○' else '○'
        
    def get_legal_moves(self) -> list[tuple[int, int]]:
        """
        Get a list of all legal moves for the current player.
        
        Returns:
            list: A list of all legal moves for the current player.
        """
        return [(x, y) for x in range(8) for y in range(8) if self.board.is_move_legal(x, y, self.current_player)]

    def reset(self):
        """
        Reset the game to its initial state by creating a new empty board and setting the current player to 'X'.
        """
        self.board = OthelloBoard()
        self.current_player = '○'
    
    def step(self, x: int, y: int) -> tuple[bool, str | None]:
        """
        Perform a game step by placing a move at the specified coordinates.

        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.

        Returns:
            tuple: A tuple containing:
                - game_over (bool): True if the game is over, False otherwise.
                - result (str or None): 1 if the current player wins, -1 if the opponent wins, 0 for a draw, or None if the game is not over.
        """
        if not self.board.is_move_legal(x, y, self.current_player):
            # If there are no legal moves for the current player, check if the game is over
            if not self.get_legal_moves():
                return True, self.check_win()
            # Otherwise, skip the player's turn
            self.switch_player()
            return False, None

        # Perform the move
        self.board.place_move(x, y, self.current_player)

        # Check for game over or switch player
        self.switch_player()
        if not self.get_legal_moves():  # Check if the opponent can move
            self.switch_player()
            if not self.get_legal_moves():  # Neither player can move
                return True, self.check_win()

        return False, None

    def _check_game_over(self) -> bool:
        """Check if the game is over."""
        return self.board.is_full() or not any(self.get_legal_moves())

    def check_win(self) -> int:
        """
        Evaluate the current state of the game when the current player places their move at (x, y).
        
        Returns:
            int: 1 if the current player wins, -1 if the opponent wins, 0 for a draw, or None if the game is not over.
        """
        if not self._check_game_over():
            return None

        black_count = sum(row.count('○') for row in self.board.board)
        white_count = sum(row.count('●') for row in self.board.board)

        if black_count > white_count:
            return 1
        elif white_count > black_count:
            return -1
        else:
            return 0  # Draw
    
    def render(self):
        """
        Render the current state of the game by displaying the Tic-Tac-Toe board.
        """
        self.board.display()
        
    def evaluate(self) -> int:
        """
        Evaluate the Othello board for the current player.
        
        Returns:
            int: The evaluation score for the current player.
        """
        black_count = sum(row.count('○') for row in self.board.board)
        white_count = sum(row.count('●') for row in self.board.board)

        if self.current_player == '○':
            return black_count - white_count
        else:
            return white_count - black_count