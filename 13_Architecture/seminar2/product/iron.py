from .item_interface import ItemInterface


class Iron(ItemInterface):
    def open(self) -> None:
        print('Iron!')