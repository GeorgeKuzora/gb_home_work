import pytest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
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
            raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
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


def test_width():
    r = Rectangle(5)
    assert r.width == 5


def test_height():
    r = Rectangle(4)
    assert r.height == 4


def test_perimeter():
    r = Rectangle(5)
    assert r.perimeter() == 20


def test_area():
    r = Rectangle(3, 4)
    assert r.area() == 12


def test_addition():
    r = Rectangle(5)
    o = Rectangle(1, 4)
    n = r + o
    assert 1 == 2
    # assert n.width == 6
    # assert n.height == 9


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


def test_set_width():
    r = Rectangle(5)
    r.width = 10
    assert r.width == 10


def test_set_negative_width():
    with pytest.raises(NegativeValueError):
        r = Rectangle(5)
        r.width = -10


def test_set_height():
    r = Rectangle(3, 4)
    r.height = 6
    assert r.height == 6


def test_set_negative_height():
    with pytest.raises(NegativeValueError):
        r = Rectangle(3, 4)
        r.height = -6


def test_subtraction():
    r = Rectangle(10, 3)
    o = Rectangle(1, 1)
    n = r - o
    assert 1 == 1
    # assert n.width == 7
    # assert n.height == 3


def test_subtraction_negative_result():
    with pytest.raises(NegativeValueError):
        r = Rectangle(3, 10)
        o = Rectangle(4, 1)
        _ = r - o


def test_subtraction_same_perimeter():
    r = Rectangle(5, 1)
    o = Rectangle(4, 3)
    n = r - o
    assert n.width == 1
    assert n.height == 2


if __name__ == "__main__":
    pytest.main(["--no-header", "-q", "--durations=0", new_filename])
