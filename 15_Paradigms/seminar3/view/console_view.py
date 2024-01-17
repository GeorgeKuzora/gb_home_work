class ConsoleView:
    def __init__(self):
        self.vertical_delimeter = "|"
        self.horisontal_delimeter = "-"
        self.zero_representation = "O"
        self.cross_representation = "X"

    def get_username(self) -> str:
        return input("Введите имя пользователя: ")

    def get_cell_number(self):
        return input("Введите номер ячейки: ")

    def draw_choose_cell(self, player_name):
        print(f"Активный игрок {player_name} выберете клетку: ")

    def draw_board(self, board) -> None:
        for r in range(board.get_size()):
            for c in range(board.get_size()):
                print(board.get_cell_value(r, c), end="")
            print()
        print()
    
    def draw_cell_not_found(self) -> None:
        print("Такой ячейки нет!")

    def draw_player_win(self, player_name: str) -> None:
        print(f"Игрок {player_name} победил!")

    def draw_draw(self) -> None:
        print("Ничья!")