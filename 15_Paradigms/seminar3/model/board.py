from model.cell import Cell
from exceptions import CellNotFoundException


class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = []

    def setup_board(self):
        count = 1
        for r in range(self.size):
            self.board.append([])
            for c in range(self.size):
                self.board[r].append(Cell(initial_value=str(count)))
                count += 1

    def get_size(self):
        return self.size

    def get_board(self):
        return self.board

    def get_cell_value(self, row_id: int, col_id: int) -> str:
        return str(self.get_board()[row_id][col_id].get_value())

    def mark_cell(self, cell_value, new_cell_value) -> None:
        for r in range(self.size):
            for c in range(self.size):
                if self.get_cell_value(r, c) == cell_value:
                    self.get_board()[r][c].set_value(new_cell_value)
                    return
        raise CellNotFoundException

    def is_full_line(self) -> bool:
        current_row = set()
        for r in range(self.size):
            for c in range(self.size):
                current_row.add(self.get_board()[r][c].get_value())
            if len(current_row) == 1:
                return True
            current_row = set()

        current_col = set()
        for c in range(self.size):
            for r in range(self.size):
                current_col.add(self.get_board()[r][c].get_value())
            if len(current_col) == 1:
                return True
            current_col = set()

        current_diag = set()
        for d in range(self.size):
            current_diag.add(self.get_board()[d][d].get_value())
        if len(current_diag) == 1:
            return True
        
        current_back_diag = set()
        for b in range(self.size):
            current_back_diag.add(self.get_board()[b][self.size-1-b].get_value())
        if len(current_diag) == 1:
            return True

        return False

    def is_no_free_cells(self):
        current_table = set()
        for r in range(self.size):
            for c in range(self.size):
                current_table.add(self.get_board()[r][c].get_value())
        if len(current_table) == 2:
            return True
        
        return False
            
