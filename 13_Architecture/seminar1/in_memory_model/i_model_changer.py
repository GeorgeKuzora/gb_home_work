from abc import ABC, abstractmethod


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender: "IModelChanger") -> None:
        pass
