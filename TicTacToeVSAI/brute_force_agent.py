import random

class BruteForceAgent:
    def __init__(self, game):
        self.game = game
    
    def choice(self, board):
        # Try to win
        for i, j in self.game.get_available_pos(board):
            board[i][j] = "O"
            if self.game.check_win(board, "O"):
                return i,j
            board[i][j] = " "

        # Blocks player
        for i, j in self.game.get_available_pos(board):
            board[i][j] = "X"
            if self.game.check_win(board, "X"):
                return i,j
            board[i][j] = " "
        
        return random.choice(self.game.get_available_pos(board))
