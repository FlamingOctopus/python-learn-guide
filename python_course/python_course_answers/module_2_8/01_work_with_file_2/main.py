import os
from typing import TextIO


class File:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def __enter__(self) -> TextIO:
        if not os.path.exists(self.file_name):
            self.file = open(self.file_name, 'w')
            print(f'Создан {self.file_name} и открыт для записи')

        else:
            print(f'{self.file_name} уже существует')
            self.file = open(self.file_name, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is Exception:
            return True


with File('file.txt') as file:
    file.write('something')
