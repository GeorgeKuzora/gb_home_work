from pathlib import Path

text = """import csv
import json
import random


def generate_csv_file(file_name, rows):
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        for _ in range(rows):
            writer.writerow(
                [
                    random.randint(-100, 100),
                    random.randint(-100, 100),
                    random.randint(-100, 100),
                ]
            )


def save_to_json(func):
    def wrapper(*args, **_):
        file_name = args[0]
        output = []
        with open(file_name, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                a, b, c = row
                a, b, c = int(a), int(b), int(c)
                output.append({"parameters": [a, b, c], "result": func(a, b, c)})
        with open("results.json", "w", encoding="utf-8") as j:
            json.dump(output, j)
        return output

    return wrapper


@save_to_json
def find_roots(a, b, c):
    # a*x^2 + b*x + c = 0
    if a == 0 and b != 0:
        return (-c) / b
    elif a == 0 and b == 0:
        return None

    d = b**2 - 4 * a * c

    if d < 0:
        return None
    elif d == 0:
        return (-b) / (2 * a)
    else:
        return (-b + d) / (2 * a), (-b - d) / (2 * a)
"""


def create_init(text):
    file_name = "__init__.py"
    p = Path(".")
    file = p / file_name
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(text)


create_init(text)
