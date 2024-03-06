class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        s = ""
        for r in range(self.rows):
            t = ""
            for c in range(self.cols):
                t += f"{self.data[r][c]} "
            t.strip(" ")
            s += t
            s += "\n"
        return s[:-2]

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for row in range(self.rows):
            if self.data[row] != other.data[row]:
                return False
        return True

    def __add__(self, other):
        inst = None
        if self.rows == other.rows or self.cols == other.cols:
            inst = Matrix(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    inst.data[r][c] = self.data[r][c] + other.data[r][c]
        return inst

    def __mul__(self, other):
        if self.rows == other.cols:
            return None

        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]

        inst = Matrix(self.rows, self.cols)
        inst.data = result
        return inst


if __name__ == "__main__":
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)

    print(matrix2)

    # Сравниваем матрицы
    print(matrix1 == matrix2)

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)
    print("----")
