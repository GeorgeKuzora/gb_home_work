from controller.game import Game
from model.board import Board
from model.player import Player
from view.console_view import ConsoleView

board = Board(size=3)
player_one = Player()
player_two = Player()
printer = ConsoleView()
game = Game(board, player_one, player_two, printer)
game.setup()
game.run()