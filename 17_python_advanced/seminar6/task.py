# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
#
#
# def is_attacking(q1, q2):
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
#
# def check_queens(queens):
#     for i in range(len(queens)):
#         for j in range(i + 1, len(queens)):
#             if is_attacking(queens[i], queens[j]):
#                 return False
#     return True
#
#
# print(check_queens(queens))


import random


def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


# board_list = []
#
# while len(board_list) < 4:
#     queens = []
#     for _ in range(8):
#         queens.append((random.randint(0, 7), random.randint(0, 7)))
#
#     if check_queens(queens):
#         board_list.append(queens)


def generate_boards():
    return [
        [(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
        [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
        [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
        [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)],
    ]


print(generate_boards())
