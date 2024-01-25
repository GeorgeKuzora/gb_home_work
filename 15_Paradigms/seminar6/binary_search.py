def binary_search(array: list, value: int) -> int:
    id_left = 0
    id_right = len(array) - 1
    while id_left <= id_right:
        id_pivot = (id_right + id_left) // 2
        if value == array[id_pivot]:
            return id_pivot
        elif value < array[id_pivot]:
            id_right = id_pivot - 1
        elif value > array[id_pivot]:
            id_left = id_pivot + 1
    return -1


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    values = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for v in values:
        print(f"Значение: {v} Индекс: {binary_search(array, v)}")
