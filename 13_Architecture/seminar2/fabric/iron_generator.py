from product.iron import Iron
from .item_generator_interface import ItemGeneratorInterface


class IronGenerator(ItemGeneratorInterface):
    def create_item(self) -> Iron:
        return Iron()