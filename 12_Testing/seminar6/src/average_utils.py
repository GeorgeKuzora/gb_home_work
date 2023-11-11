"""
Модуль для расчета и сравнения среднего значения чисел, представленных
в виде списка
"""


class AverageUtils:
    """
    Модуль для расчета и сравнения среднего значения чисел, представленных
    в виде списка
    """

    @staticmethod
    def find_average(numbers: list[int | float]) -> float:
        """
        Метод для расчета среднего значения чисел в списке.

        Args:
            numbers: Список с числами.

        Returns:
            Среднее значение всех чисел в списке.

            Может выбрасывать исключения TypeError.
        """
        if not isinstance(numbers, list):
            raise TypeError(f"expected list but got {type(numbers)}")
        if not numbers:
            return 0
        try:
            return sum(numbers) / len(numbers)
        except TypeError as e:
            raise TypeError("list should contain only numbers") from e

    @staticmethod
    def compare_average(
        first: list[int | float], second: list[int | float]
    ) -> None:
        """
        Метод для сравнения среднего значения чисел в двух списках.

        Args:
            first: Список с числами.
            second: Список с числами.

        Может выбрасывать исключения TypeError.
        """
        first_average = AverageUtils.find_average(first)
        second_average = AverageUtils.find_average(second)
        if first_average > second_average:
            print("Первый список имеет большее среднее значение")
        elif first_average < second_average:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")
