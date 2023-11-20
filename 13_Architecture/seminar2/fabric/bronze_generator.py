from product.bronze import Bronze
from .item_generator_interface import ItemGeneratorInterface


class BronzeGenerator(ItemGeneratorInterface):
    def create_item(self) -> Bronze:
        return Bronze()