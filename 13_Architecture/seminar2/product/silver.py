from .item_interface import ItemInterface


class Silver(ItemInterface):
    def open(self) -> None:
        print('Silver!')