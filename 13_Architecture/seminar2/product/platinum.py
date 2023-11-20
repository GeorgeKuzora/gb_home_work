from .item_interface import ItemInterface


class Platinum(ItemInterface):
    def open(self) -> None:
        print('Platinum!')