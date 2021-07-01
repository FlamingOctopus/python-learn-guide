import os

path = os.path.abspath('/home/def/PycharmProjects/python_basic_15')
find_path = "custom_25"


#
# def gen_files_path(find_path: str, path: str = "/", ) -> str:
#     for obj in os.listdir(path):
#         path_obj = f"{path}/{obj}"
#         if obj == find_path:
#             print("Папка найдена")
#             return
#         if os.path.isdir(path_obj):
#             yield from gen_files_path(find_path, path_obj)
#         else:
#             yield path_obj
#
#
# for i in gen_files_path(find_path, path):
#     print(i)
# Первый вариант через yield from

def gen_files_path(find_path: str, path: str = os.path.abspath(os.path.sep)) -> str:
    for obj in os.listdir(path):
        path_obj = os.path.join(path, obj)
        if obj == find_path:
            print("Папка найдена")
            return
        else:
            yield path_obj
        if os.path.isdir(path_obj):
            for dir in gen_files_path(find_path, path_obj):
                yield dir


for i in gen_files_path(find_path, path):
    print(i)
