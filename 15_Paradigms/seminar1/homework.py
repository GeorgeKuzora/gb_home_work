def sort_imperative(arr):
    for i in range(len(arr), -1, -1):
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort_decratative(arr):
    return sorted(arr)


if __name__ == "__main__":
    arr = [9, 3, 5, 2, 5, 6, 0, 1]
    print(sort_imperative(arr))
    print(sort_decratative(arr))
