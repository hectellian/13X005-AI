from assignment3.games.othello.game import OthelloGame

class OthelloGameModified(OthelloGame):
    def __init__(self):
        super().__init__()
    
    def evaluate(self) -> float:
        """
        Evaluate the current state of the game from the perspective of the current player.

        Returns:
            float: The evaluation value.
        """
        positional_weights = [
            [ 4, -3, 2, 2, 2, 2, -3,  4],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [ 2, -1,  1,  0,  0,  1, -1,  2],
            [ 2, -1,  0,  1,  1,  0, -1,  2],
            [ 2, -1,  0,  1,  1,  0, -1,  2],
            [ 2, -1,  1,  0,  0,  1, -1,  2],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [ 4, -3,  2,  2,  2,  2, -3,  4]
        ]
        
        player_score = opponent_score = 0
        opponent_symbol = '○' if self.current_player == '●' else '●'

        for x in range(8):
            for y in range(8):
                if self.board.board[x][y] == self.current_player:
                    player_score += positional_weights[x][y]
                elif self.board.board[x][y] == opponent_symbol:
                    opponent_score += positional_weights[x][y]

        return player_score - opponent_score