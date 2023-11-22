from assignment3.interfaces.game import IGame
from assignment3.games.tic_tac_toe.board import TicTacToeBoard

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
        
    def switch_player(self):
        """
        Switch the current player.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    def get_legal_moves(self) -> list[tuple[int, int]]:
        """
        Get a list of all legal moves for the current player.
        
        Returns:
            list: A list of all legal moves for the current player.
        """
        return [(x, y) for x in range(3) for y in range(3) if self.board.is_move_legal(x, y)]

    def reset(self):
        """
        Reset the game to its initial state by creating a new empty board and setting the current player to 'X'.
        """
        self.board = TicTacToeBoard()
        self.current_player = 'X'

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
        if not self.board.place_move(x, y, self.current_player): # Places the move if true and continues, else returns false
            return False, None 

        win_state = self.check_win(x, y)
        if win_state is not None:
            return True, win_state

        self.switch_player()
        
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

    def check_win(self, x: int, y: int) -> int:
        """
        Evaluate the current state of the game when the current player places their move at (x, y).
        
        Returns:
            int: 1 if the current player wins, -1 if the opponent wins, 0 for a draw, or None if the game is not over.
        """
        if self._check_win(x, y):
            return 1
        opponent = 'O' if self.current_player == 'X' else 'X'
        if any(self._check_win(i, j) for i in range(3) for j in range(3) if self.board.board[i][j] == opponent):
            return -1
        if self.board.is_full():
            return 0
        return None
    
    def render(self):
        """
        Render the current state of the game by displaying the Tic-Tac-Toe board.
        """
        self.board.display()
        
    def evaluate(self) -> int:
        """
        Evaluate the Tic-Tac-Toe board for the current player.
        f(v) = (# open lines/columns/diagonals for MAX) - (# open lines/columns/diagonals for MIN)
        
        Returns:
            int: The evaluation score for the current player.
        """
        board = self.board.board
        lines = board + [list(col) for col in zip(*board)]  # Rows and Columns
        diagonals = [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]

        def count_open_for_player(player):
            return sum(
                all(cell != player for cell in line) for line in lines
            ) + sum(
                all(cell != player for cell in diag) for diag in diagonals
            )

        open_count_max = count_open_for_player('O')  # Open lines/columns/diagonals for 'X'
        open_count_min = count_open_for_player('X')  # Open lines/columns/diagonals for 'O'

        return open_count_max - open_count_min