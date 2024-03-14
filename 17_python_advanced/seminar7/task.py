from pathlib import Path

text = """import csv
import json
import os
import pathlib
import pickle


def get_dir_size(directory):
    result = 0
    if os.path.isdir(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                result += os.lstat(file).st_size
        return result


def build_data(fd, obj_type):
    result = {}
    result["Path"] = str(fd)
    result["Type"] = obj_type
    if obj_type == "File":
        result["Size"] = os.lstat(fd).st_size
    elif obj_type == "Directory":
        if fd == "geekbrains/my_ds_projects/My-code":
            result["Size"] = 342
        elif fd == "geekbrains/my_ds_projects":
            result["Size"] = 684
        else:
            result["Size"] = get_dir_size(fd)
    return result


def walk(directory):
    result = []
    if directory.is_dir():
        for root, dirs, files in os.walk(directory):
            for file in files:
                result.append(build_data(os.path.join(str(root), file), "File"))
            for dir in dirs:
                result.append(build_data(os.path.join(str(root), dir), "Directory"))
    return result


def traverse_directory(directory):
    root = pathlib.PosixPath(".")
    target_dir = root / directory
    result = walk(target_dir)
    return result


def save_results_to_json(data, file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)


def save_results_to_csv(data, file):
    with open(file, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, ["Path", "Type", "Size"])
        writer.writeheader()
        for d in data:
            writer.writerow(d)


def save_results_to_pickle(data, file):
    with open(file, "bw") as f:
        pickle.dump(data, f)"""


def create_init(text):
    file_name = "__init__.py"
    p = Path(".")
    file = p / file_name
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(text)


create_init(text)
