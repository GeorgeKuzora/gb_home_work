from .item_interface import ItemInterface


class Wood(ItemInterface):
    def open(self) -> None:
        print('Wood!')