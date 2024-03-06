class Rectangle:
    def __init__(self, width, height=None) -> None:
        self.width = width
        if height:
            self.height = height
        else:
            self.height = width

    def perimeter(self):
        return self.height * 2 + self.width * 2

    def area(self):
        return self.height * self.width

    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width, height)

    def __sub__(self, other):
        width = abs(self.width - other.width)
        height = abs(self.height - other.height)
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
