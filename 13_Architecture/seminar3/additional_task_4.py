# Переписать код в соответствии с Liskov Substitution Principle:

from abc import ABC, abstractmethod


class Shape2D(ABC):
    """
    Прямоугольник и квадрат обладают разными свойствами.
    Они не отвечают принципу подстановки Лисков.
    Мы не можем позволить указывать различные значения для высоты
    и ширины квадрата. Он должен обладать только одним полем side.
    Эти две фигуры объединяет возможность подсчета площади фигуры.
    """
    @abstractmethod
    def area(self):
        raise NotImplementedError("Method is not implemented")
    

class Rectangle(Shape2D):
    def init(self):
        self.width = 0
        self.height = 0

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def init(self):
        self.side = 0

    def setSide(self, side):
        self.side = side

    def area(self):
        return self.side^2