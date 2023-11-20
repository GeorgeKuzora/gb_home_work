from .item_interface import ItemInterface


class Gem(ItemInterface):
    def open(self) -> None:
        print('Gem!')