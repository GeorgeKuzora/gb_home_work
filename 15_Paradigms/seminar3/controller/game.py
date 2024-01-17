from enum import Enum
from model.board import Board
from model.player import Player
from model.cell import Cell
from view.console_view import ConsoleView
from exceptions import(
    CellNotFoundException
)


class Game:
    
    GAME_STATUS = Enum('GameStatus', ['RUNNING', 'DRAW', 'PLAYER_ONE_WIN', 'PLAYER_TWO_WIN'])
    
    def __init__(self, board: Board, player_one: Player, player_two: Player, view: ConsoleView) -> None:
        self.board = board
        self.player_one = player_one
        self.player_two = player_two
        self.active_player = player_one
        self.view = view
        self.game_status = self.GAME_STATUS.RUNNING
            
    def setup(self) -> None:
        self.player_one.set_using_zeros()
        self.player_two.set_using_crosses()
        
        player_one_username = self.view.get_username()
        player_two_username = self.view.get_username()

        self.player_one.set_name(player_one_username)
        self.player_two.set_name(player_two_username)

        self.board.setup_board()

    def run(self) -> None:
        while self.game_status == self.GAME_STATUS.RUNNING:
            self.make_move()
    
    def make_move(self) -> None:
        self.view.draw_choose_cell(self.active_player.get_name())
        self.view.draw_board(self.board)
        self.choose_cell()
        self.update_game_status()
        if self.game_status != self.GAME_STATUS.RUNNING:
            self.publish_results()
            return
        self.change_active_player()

    def choose_cell(self):
        cell_number = self.view.get_cell_number()
        if (cell_number == self.player_one.get_character_value()
            or cell_number == self.player_two.get_character_value()):
            self.view.draw_cell_not_found()
            return self.choose_cell()
        try:
            self.board.mark_cell(cell_number, self.active_player.get_character_value())
        except CellNotFoundException:
            self.view.draw_cell_not_found()
            return self.choose_cell()

    def update_game_status(self) -> None:
        if self.board.is_full_line():
            self.decide_winner()
        elif self.board.is_no_free_cells():
            self.decide_draw()

    def decide_winner(self) -> None:
        if self.active_player is self.player_one:
            self.game_status = self.GAME_STATUS.PLAYER_ONE_WIN
        else:
            self.game_status = self.GAME_STATUS.PLAYER_TWO_WIN

    def decide_draw(self):
        self.game_status = self.GAME_STATUS.DRAW

    def publish_results(self):
        if self.game_status == self.GAME_STATUS.PLAYER_ONE_WIN or self.game_status == self.GAME_STATUS.PLAYER_TWO_WIN:
            self.view.draw_player_win(self.active_player.get_name())
            self.view.draw_board(self.board)
        elif self.game_status == self.GAME_STATUS.DRAW:
            self.view.draw_draw()
            self.view.draw_board(self.board)

    def change_active_player(self) -> None:
        if self.active_player is self.player_one:
            self.active_player = self.player_two
        else:
            self.active_player = self.player_one