from product.silver import Silver
from .item_generator_interface import ItemGeneratorInterface


class SilverGenerator(ItemGeneratorInterface):
    def create_item(self) -> Silver:
        return Silver()