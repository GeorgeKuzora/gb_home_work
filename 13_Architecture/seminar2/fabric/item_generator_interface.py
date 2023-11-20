from abc import ABC, abstractmethod
from product.item_interface import ItemInterface

class ItemGeneratorInterface(ABC):
    @abstractmethod
    def create_item(self) -> ItemInterface:
        raise NotImplementedError("Method create_item was not implemented")