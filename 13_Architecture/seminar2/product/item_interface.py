from abc import ABC, abstractmethod

class ItemInterface(ABC):
    @abstractmethod
    def open(self) -> None:
        raise NotImplementedError("Method open was not implemented")