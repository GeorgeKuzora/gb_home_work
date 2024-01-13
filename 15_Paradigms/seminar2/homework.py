"""
Я выбрал процедурную парадигму. Процедурная парадигма позволяет разбить
программу на функции и процедуры. Тем самым это позволяет лучше организовать
код и добиться большей выразительности. Также использование функций позволяет
использовать уже написанный код повторно.
"""


def get_number() -> int:
    console_input = input("Введите число: ")
    try:
        number = int(console_input)
    except ValueError:
        print("Введено недопустимое значение")
        return get_number()
    return number


def calculate_multiplication_table(number: int) -> list[tuple[int, int, int]]:
    multiplication_table = []
    for i in range(1, 10):
        multiplication_table.append((number, i, number * i))
    return multiplication_table


def print_multiplication_table(
    multiplication_table: list[tuple[int, int, int]]
) -> None:
    for number, multiplucator, multiplication in multiplication_table:
        print(f"{number} * {multiplucator} = {multiplication}")


if __name__ == "__main__":
    number = get_number()
    table = calculate_multiplication_table(number)
    print_multiplication_table(table)
