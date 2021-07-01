import os
from typing import Iterable


def gen_string_couter(path: dir) -> Iterable:
    for file in os.listdir(path):
        if os.path.isfile(file) and file.endswith(".py"):
            with open(os.path.abspath(file), 'r') as current_py_file:
                count_str = 0
                tuple_start = ("\n", "#")
                for string in current_py_file.readlines():
                    if string.startswith(tuple_start):
                        continue
                    count_str += 1
                yield f"В файле {file} - {count_str} строк"


path = "/home/def/PycharmProjects/python_basic_15/Module19/01_songs_2"
for i in gen_string_couter(path):
    print(i)
