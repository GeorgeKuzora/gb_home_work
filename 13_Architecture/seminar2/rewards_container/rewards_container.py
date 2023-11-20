from random import randint

from .rewards_container_interface import RewardsContainerInterface
from fabric.gold_generator import GoldGenerator
from fabric.gem_generator import GemGenerator
from fabric.bronze_generator import BronzeGenerator
from fabric.iron_generator import IronGenerator
from fabric.platinum_generator import PlatinumGenerator
from fabric.silver_generator import SilverGenerator
from fabric.wood_generator import WoodGenerator


class RewardsContainer(RewardsContainerInterface):
    """
    A container for producing different products with different
    probability to be produced.
    """

    def getRewards(self) -> None:
        """
        Produces products with following probabilities:
        Wood - 10/53
        Iron - 10/53
        Bronze - 10/53
        Silver - 10/53
        Platinum - 10/53
        Gold - 3/53
        Gem - 1/53
        """
        rand = randint(1, 54)
        if rand <= 10:
            return WoodGenerator().create_item().open()
        if rand <= 20:
            return IronGenerator().create_item().open()
        if rand <= 30:
            return BronzeGenerator().create_item().open()
        if rand <= 40:
            return SilverGenerator().create_item().open()
        if rand <= 50:
            return PlatinumGenerator().create_item().open()
        if rand <= 53:
            return GoldGenerator().create_item().open()
        if rand <= 54:
            return GemGenerator().create_item().open()