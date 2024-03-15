import argparse
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f"Rectangle was created with negative width {width}")
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f"Rectangle was created with negative height {height}")
                raise NegativeValueError(
                    f"Высота должна быть положительной, а не {height}"
                )
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            logger.error(f"Negative value {value} was set to width")
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            logger.error(f"Negative value {value} was set to height")
            raise NegativeValueError(f"Высота должна быть положительной, а не {value}")

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self) -> str:
        return f"Rectagle has width={self.width} and height={self.height}"


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def birthday(self):
        self._age += 1

    def get_age(self):
        logger.info(f"method get_age was called of Person object{self}")
        return self._age


class Employee(Person):
    def __init__(
        self,
        last_name: str,
        first_name: str,
        patronymic: str,
        age: int,
        position: str,
        salary: float,
    ):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= 1 + percent / 100

    def __str__(self):
        return f"{self.full_name()} ({self.position})"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Simple program", description="Simple argument parser"
    )
    parser.add_argument(
        "--rectangle", action="store_true", help="Create and output rectangle"
    )
    parser.add_argument("-w", "--width", help="Set rectangle width")
    parser.add_argument("-d", "--height", help="Set rectangle height")
    args = parser.parse_args()
    if args.rectangle:
        if args.width and args.height:
            w = float(args.width)
            h = float(args.height)
            print(Rectangle(w, h))
        elif args.width:
            w = float(args.width)
            print(Rectangle(w))
        else:
            print("Not enough arguments")
    else:
        print("action was not chosen")
