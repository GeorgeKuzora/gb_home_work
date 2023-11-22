# Переписать код в соответствии с Interface Segregation Principle:

from abc import ABC, abstractmethod
import math


class Shape2D(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Method is not implemented")


class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        raise NotImplementedError("Method is not implemented")


class Circle(Shape2D):
    def init(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(Shape3D):
    def init(self, edge):
        self.edge = edge

    def volume(self):
        return self.edge * self.edge * self.edge