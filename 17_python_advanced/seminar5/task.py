def fibonacci():
    fib0 = 0
    fib1 = 1
    yield fib0
    yield fib1
    while True:
        fib0, fib1 = fib1, fib0+fib1
        yield fib1


if __name__ == "__main__":
    f = fibonacci()
    for i in range(10):
        print(next(f))
