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

    def place_move(self, x, y, symbol):
        """
        Place a move on the board at position (x, y) with the given symbol.
        
        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
            symbol (str): The symbol to place ('X', 'O').

        Returns:
            bool: True if the move was placed successfully, False otherwise.
        """
        if self.board[x][y] == ' ':
            self.board[x][y] = symbol
            return True
        else:
            return False

    def is_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def display(self):
        """
        Display the current state of the board.
        """
        for row in self.board:
            print(" | ".join(row))
