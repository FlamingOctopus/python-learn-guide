from collections import OrderedDict
import zipfile


def unzip(zip):
    file = zipfile.ZipFile(zip, 'r')
    for file_zip in file.namelist():
        file.extract(file_zip)
        file_r = file_zip
    file.close()
    return file_r


def make_dict(filename):
    with open(filename, 'r') as file:
        file = file.readlines()
        count = 0
        syms_dict = {}
        for row in file:
            for sym in row:
                if sym.isalpha():
                    if sym in syms_dict:
                        syms_dict[sym] += 1
                    else:
                        syms_dict[sym] = 1
                    count += 1
        return syms_dict


def sort_syms(syms_dict):
    syms_dict = OrderedDict(sorted(syms_dict.items(), key=lambda x: x[1], reverse=True))
    return syms_dict


def main_func(zip_file):
    final_dict = sort_syms(make_dict(unzip(zip_file)))
    print("БУКВА | КОЛИЧЕСТВО")
    for letter, count in final_dict.items():
        print(f"  {letter}   |  {count}")


main_func('voyna-i-mir.zip')
