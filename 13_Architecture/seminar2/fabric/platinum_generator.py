from product.platinum import Platinum
from .item_generator_interface import ItemGeneratorInterface


class PlatinumGenerator(ItemGeneratorInterface):
    def create_item(self) -> Platinum:
        return Platinum()