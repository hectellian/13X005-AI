from assignment3.games.tic_tac_toe.board import TicTacToeBoard
from assignment3.games.tic_tac_toe.game import TicTacToeGame
from assignment3.interfaces.game import IGame

class Minimax:
    """
    Minimax algorithm with Alpha-Beta pruning for use in two-player games like Tic-Tac-Toe.

    Attributes:
        game (TicTacToeGame): An instance of the game for which the Minimax algorithm is applied.
    """

    def __init__(self, game: IGame):
        """
        Initialize the Minimax algorithm with a game instance.

        Parameters:
            game (IGame): The game instance.
        """
        self.game = game

    def search(self, depth: int, alpha: float, beta: float, maximizing_player: bool) -> tuple[float, tuple[int, int] | None]:
        """
        Perform the Minimax search with Alpha-Beta pruning.

        Parameters:
            depth (int): The maximum depth of the game tree to explore.
            alpha (float): The best value that the maximizer currently can guarantee (initialized to -infinity).
            beta (float): The best value that the minimizer currently can guarantee (initialized to infinity).
            maximizing_player (bool): True if the current turn is of the maximizing player, False otherwise.

        Returns:
            tuple: A tuple containing the best score and the corresponding best move.
        """
        if depth == 0 or not self.game.get_legal_moves():
            return self.game.evaluate(), None

        if maximizing_player:
            return self._maximize(depth, alpha, beta)
        else:
            return self._minimize(depth, alpha, beta)

    def _maximize(self, depth: int, alpha: float, beta: float) -> tuple[float, tuple[int, int] | None]:
        """
        Maximize the utility for the maximizing player.
        """
        max_eval = float('-inf')
        best_move = None
        for move in self.game.get_legal_moves():
            self.game.board.place_move(*move, self.game.current_player)
            eval, _ = self.search(depth - 1, alpha, beta, False)
            self.game.board.undo_move(*move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move

    def _minimize(self, depth: int, alpha: float, beta: float) -> tuple[float, tuple[int, int] | None]:
        """
        Minimize the utility for the minimizing player.
        """
        min_eval = float('inf')
        best_move = None
        for move in self.game.get_legal_moves():
            self.game.board.place_move(*move, self.game.current_player)
            eval, _ = self.search(depth - 1, alpha, beta, True)
            self.game.board.undo_move(*move)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
