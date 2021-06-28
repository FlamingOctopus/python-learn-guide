def start_validate(file_name):
    string_symbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
    return file_name.startswith(string_symbols)


def end_validate(file_name):
    postfix = ('.txt', '.docx')
    return file_name.endswith(postfix)


file_name = input("Название файла: ")
start_check = start_validate(file_name)
end_check = end_validate(file_name)

if start_check and end_check:
    print("Ошибка: название начинается на один из специальных символов")
elif start_check and not end_check:
    print("неверное расширение файла. Ожидалось .txt или .docx\n\
    Ошибка: название начинается на один из специальных символов")
elif not start_check and not end_check:
    print("неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно.")
