from game import Game
from brute_force_agent import BruteForceAgent

game = Game()
agent = BruteForceAgent(game)

game.play_with(agent)
