from assignment3.interfaces.board import IBoard

class TicTacToeBoard(IBoard):
    """
    Class representing a Tic-Tac-Toe game board.
    This class inherits from the AbstractBoard class and implements its abstract methods.
    """

    def __init__(self):
        """
        Initialize a 3x3 Tic-Tac-Toe board filled with empty spaces.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
    def is_move_legal(self, x, y):
        """Check if a move is legal.
        
        Parameters
        ----------
        x : int
            The row index for the move.
        y : int
            The column index for the move.
            
        Returns
        -------
        bool
            True if the move is legal, False otherwise.
        """
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '

    def place_move(self, x: int, y: int, symbol: str) -> bool:
        """
        Place a move on the board at position (x, y) with the given symbol.
        
        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
            symbol (str): The symbol to place ('X', 'O').

        Returns:
            bool: True if the move was placed successfully, False otherwise.
        """
        if self.is_move_legal(x, y):
            self.board[x][y] = symbol
            return True
        else:
            return False
        
    def undo_move(self, x, y):
        """Undo a move at position (x, y).

        Parameters
        ----------
        x : int
            The row index for the move.
        y : int
            The column index for the move.
        """
        self.board[x][y] = ' '

    def is_full(self) -> bool:
        """
        Check if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != ' ' for row in self.board for cell in row)

    def display(self):
        """
        Display the current state of the board.
        """
        print("   0   1   2")  # Column labels
        for i, row in enumerate(self.board):
            print(" +---+---+---+")
            print(f"{i}| {' | '.join(row)} |")  # Row number and board row
        print(" +---+---+---+")