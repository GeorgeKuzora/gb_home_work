from .item_interface import ItemInterface


class Gold(ItemInterface):
    def open(self) -> None:
        print('Gold!')