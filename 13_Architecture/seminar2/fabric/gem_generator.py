from product.gem import Gem
from .item_generator_interface import ItemGeneratorInterface


class GemGenerator(ItemGeneratorInterface):
    def create_item(self) -> Gem:
        return Gem()