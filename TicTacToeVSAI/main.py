from game import Game
import random

def play():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Welcome!")
    Game.show_board_status(board)

play()