import os

path = os.path.abspath('/home/def/PycharmProjects/python_basic_15/Module21')


def walk(path, list_dirs=[], list_files=[], size=[]):
    for obj in os.listdir(path):

        if os.path.isdir(f"{path}/{obj}"):
            list_dirs.append(obj)
            walk(f"{path}/{obj}", list_dirs, list_files, size)
        else:
            size.append(os.path.getsize(f'{path}/{obj}'))
            list_files.append(obj)
    return (len(list_dirs), len(list_files), sum(size))


dir_count, file_count, size = walk(path)

print("Размер каталога (в Кб):", size / 1024)
print("Количество подкаталогов:", dir_count)
print("Количество файлов:", file_count)
