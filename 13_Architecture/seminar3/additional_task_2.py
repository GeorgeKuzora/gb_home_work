# Переписать код SpeedCalculation в соответствии с Open-Closed Principle:

from abc import ABC, abstractmethod


class SpeedPolicy(ABC):
    """
    Класс для задания коэффициентов скорости для различных ситуаций.
    Например для автомобиля при езде в тумане, либо для автобуса при езде
    в горах и тд.
    """
    ALLOWED_SPEED_COEF = 0.0


class CarSpeedPolicy(SpeedPolicy):
    """
    Класс для задания коэффициентов скорости для различных ситуаций.
    Например для автомобиля при езде в тумане, либо для автобуса при езде
    в горах и тд.
    """
    ALLOWED_SPEED_COEF = 0.8


class BusSpeedPolicy(SpeedPolicy):
    """
    Класс для задания коэффициентов скорости для различных ситуаций.
    Например для автомобиля при езде в тумане, либо для автобуса при езде
    в горах и тд.
    """
    ALLOWED_SPEED_COEF = 0.6


class Vehicle(ABC):
    @abstractmethod
    def get_max_speed(self):
        raise NotImplementedError("Method is not implemented")

    @abstractmethod
    def get_type(self):
        raise NotImplementedError("Method is not implemented")

    @abstractmethod
    def calculate_allowed_speed(self, speed_policy: SpeedPolicy):
        raise NotImplementedError("Method is not implemented")


class Car(Vehicle):
    def init(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

    def calculate_allowed_speed(self, speed_policy: SpeedPolicy):
        return self.get_max_speed() * speed_policy.ALLOWED_SPEED_COEF


class Bus(Vehicle):
    def init(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type

    def calculate_allowed_speed(self, speed_policy: SpeedPolicy):
        return self.get_max_speed() * speed_policy.ALLOWED_SPEED_COEF


class SpeedCalculation:
    def calculate_allowed_speed(self, vehicle: Vehicle, speed_policy: SpeedPolicy):
        return vehicle.calculate_allowed_speed(speed_policy)
