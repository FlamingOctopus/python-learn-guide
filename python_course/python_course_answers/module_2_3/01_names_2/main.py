with open("people.txt", 'r') as file:
    file = file.readlines()
    count = 0
    with open("errors.log", 'w') as file_error:
        for id, line in enumerate(file, 1):
            try:
                line = line.replace("\n", "")
                if len(line) < 3:
                    raise Exception(f"Имя меньше 3 символов, {id} строка")
                count += len(line)
            except Exception:
                file_error.write(f"Имя меньше 3 символов, {id} строка")

    print(count)
