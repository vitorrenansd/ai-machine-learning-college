from game import Game
from math import random

class Agent:
    
    def bruteforce_agent(board):
        # Try to win
        for i, j in Game.get_available_pos(board):
            board[i][j] = "O"
            if Game.check_win(board, "O"):
                return i,j
            board[i][j] = " "

        # Blocks player
        for i, j in Game.get_available_pos(board):
            board[i][j] = "X"
            if Game.check_win(board, "X"):
                return i,j
            board[i][j] = " "
        
        return random.choice(Game.get_available_pos(board))