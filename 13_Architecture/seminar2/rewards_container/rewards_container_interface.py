from abc import ABC, abstractmethod


class RewardsContainerInterface(ABC):
    @abstractmethod
    def getRewards(self):
        raise NotImplementedError("Method get_rewards was not implemented")