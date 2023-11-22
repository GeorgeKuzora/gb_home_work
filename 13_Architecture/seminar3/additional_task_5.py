# Переписать код в соответствии с Dependency Inversion Principle:
"""Все зависимости развернуты в сторону интерфейса"""

from abc import ABC, abstractmethod


class Engine(ABC):
    def start(self):
        raise NotImplementedError("Method is not implemented")


class PetrolEngine(Engine):
    def start(self):
        pass


class DieselEngine(Engine):
    def start(self):
        pass


class Car:
    def init(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        

if __name__ == "__main__":
    petrol_engine = PetrolEngine()
    diesel_engine = DieselEngine()
    sedan = Car(petrol_engine)
    pickup = Car(diesel_engine)
    sedan.start()
    pickup.start()