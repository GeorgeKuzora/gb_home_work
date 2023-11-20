from .item_generator_interface import ItemGeneratorInterface
from product.gold import Gold


class GoldGenerator(ItemGeneratorInterface):
    def create_item(self) -> Gold:
        return Gold()