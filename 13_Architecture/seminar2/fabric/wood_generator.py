from product.wood import Wood
from .item_generator_interface import ItemGeneratorInterface


class WoodGenerator(ItemGeneratorInterface):
    def create_item(self) -> Wood:
        return Wood()