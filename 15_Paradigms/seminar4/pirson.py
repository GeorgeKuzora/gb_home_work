from functools import reduce
from math import sqrt


def calculate_pirson_corilation(array_x: list, array_y: list) -> float | None:
    if len(array_x) != len(array_y) or len(array_x) == 0 or len(array_y) == 0:
        return None

    mean_x = sum(array_x) / len(array_x)
    mean_y = sum(array_y) / len(array_y)
    # calculate divided
    both_arrays = zip(array_x, array_y)
    divided_mult_array = map(lambda z: (z[0] - mean_x) * (z[1] - mean_y), both_arrays)
    divided = sum(
        divided_mult_array,
    )
    # calculate divisor
    both_arrays = zip(array_x, array_y)
    divisor_mult_array = map(
        lambda z: ((z[0] - mean_x) ** 2) * ((z[1] - mean_y) ** 2), both_arrays
    )
    divisor_sum = sum(
        divisor_mult_array,
    )
    divisor = sqrt(divisor_sum)

    if divisor == 0:
        return None
    return divided / divisor


if __name__ == "__main__":
    array_x = [1, 2, 3, 4, 5, 6, 7]
    array_y = [1, 2, 3, 4, 5, 6, 7]
    print(calculate_pirson_corilation(array_x, array_y))
