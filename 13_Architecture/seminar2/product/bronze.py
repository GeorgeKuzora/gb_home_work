from .item_interface import ItemInterface


class Bronze(ItemInterface):
    def open(self) -> None:
        print('Bronze!')