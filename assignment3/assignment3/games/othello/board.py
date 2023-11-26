import copy
from assignment3.interfaces.board import IBoard

class OthelloBoard(IBoard):
    """
    Class representing an Othello game board.
    This class inherits from the AbstractBoard class and implements its abstract methods.
    """

    def __init__(self):
        """
        Initialize an 8x8 Othello board filled with empty spaces.
        """
        self.board = [[' ' for _ in range(8)] for _ in range(8)] # 8x8 board
        self.board[3][3], self.board[4][4] = '○', '○'
        self.board[3][4], self.board[4][3] = '●', '●'
        self.move_history = []
        
    def _captures(self, x: int, y: int, dx: int, dy: int, symbol: str, opponent: str) -> bool:
        """
        Check if placing a piece at (x, y) captures opponent pieces in a specific direction.
        
        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
            dx (int): The x direction to check.
            dy (int): The y direction to check.
            symbol (str): The symbol to place ('○', '●').
            opponent (str): The opponent's symbol.
            
        Returns:
            bool: True if the move captures at least one opponent piece, False otherwise.
        """
        i, j = x + dx, y + dy
        captured = False
        while 0 <= i < 8 and 0 <= j < 8 and self.board[i][j] == opponent:
            i, j = i + dx, j + dy
            captured = True
        return captured and 0 <= i < 8 and 0 <= j < 8 and self.board[i][j] == symbol
    
    def is_move_legal(self, x: int, y: int, symbol: str) -> bool:
        """Check if a move is legal.
        
        Parameters
        ----------
        x : int
            The row index for the move.
        y : int
            The column index for the move.
        symbol : str
            The symbol to place ('●', '○').
            
        Returns
        -------
        bool
            True if the move is legal, False otherwise.
        """
        # Check if the cell is empty
        if self.board[x][y] != ' ':
            return False

        # Check if the move captures at least one opponent piece
        opponent = '○' if symbol == '●' else '●'
        return any(
            self._captures(x, y, dx, dy, symbol, opponent)
            for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0
        )
    
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
        if not self.is_move_legal(x, y, symbol):
            return False

        # Record the move and the flipped pieces
        move_record = {'move': (x, y), 'flipped': []}
        self.board[x][y] = symbol
        opponent = '○' if symbol == '●' else '●'
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                flipped = self._flip(x, y, dx, dy, symbol, opponent)
                move_record['flipped'].extend(flipped)

        self.move_history.append(move_record)
        return True

    def _flip(self, x: int, y: int, dx: int, dy: int, symbol: str, opponent: str) -> list[tuple[int, int]]:
        """Flip pieces in a specific direction.

        Parameters:
            x (int): The row index for the move.
            y (int): The column index for the move.
            dx (int): The x direction to flip.
            dy (int): The y direction to flip.
            symbol (str): The symbol to place ('X', 'O').
            opponent (str): The opponent's symbol.
            
        Returns:
            list: A list of positions that were flipped.
        """
        flip_positions = []
        i, j = x + dx, y + dy
        while 0 <= i < 8 and 0 <= j < 8 and self.board[i][j] == opponent:
            flip_positions.append((i, j))
            i, j = i + dx, j + dy
        if 0 <= i < 8 and 0 <= j < 8 and self.board[i][j] == symbol:
            for position in flip_positions:
                self.board[position[0]][position[1]] = symbol
            return flip_positions
        return []

    def undo_move(self, *args, **kwargs) -> None:
        """Undo the last move."""
        if not self.move_history:
            return

        last_move = self.move_history.pop()
        x, y = last_move['move']
        self.board[x][y] = ' '  # Remove the last placed piece

        # Flip back the pieces
        for i, j in last_move['flipped']:
            self.board[i][j] = '○' if self.board[i][j] == '●' else '●'

    def is_full(self) -> bool:
        """
        Check if the board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all(cell != ' ' for row in self.board for cell in row)

    def display(self):
        """
        Display the current state of the Othello board
        """
        # Display the top column labels
        column_labels = '    ' + '   '.join(str(i) for i in range(8))
        print(column_labels)
        print('  +' + '---+' * 8)

        for i, row in enumerate(self.board):
            # Display the row label
            print(f"{i } |", end='')

            # Display the row contents
            for cell in row:
                char = ' ' if cell == ' ' else cell
                print(f" {char} |", end='')

            print('\n  +' + '---+' * 8)