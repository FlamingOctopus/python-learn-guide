def validator(row, list_oper):
    row = row.replace("\n", "").split(" ")
    if len(row) != 3:
        raise IndexError("Ошибка в количестве аргументов")
    if not (row[0].isdigit() and row[2].isdigit()):
        raise ValueError("Ошибка, числа должны быть целые")
    if not row[1] in list_oper:
        raise SyntaxError("Ошибка в операции")
    return True, row


def calc(first_num, oper, second_num):
    if oper == "+":
        return int(first_num) + int(second_num)
    if oper == "-":
        return int(first_num) - int(second_num)
    if oper == "*":
        return int(first_num) * int(second_num)
    if oper == "/":
        return int(first_num) / int(second_num)
    if oper == "//":
        return int(first_num) / int(second_num)
    if oper == "%":
        return int(first_num) % int(second_num)


def main(row, list_oper):
    valid = validator(row, list_oper)
    first_num, oper, second_num = valid[1]
    temp = calc(first_num, oper, second_num)
    return temp


list_oper = ['+', "-", "*", "/", "//", "%"]
summa = 0
with open("calc.txt", 'r') as file_calc:
    for row in file_calc:
        try:
            temp = main(row, list_oper)
            print(temp)
            summa += temp
        except Exception as exp:
            response = input(f"{row} - !!!  {exp}\t  Хотите исправить? ")
            if response == "да":
                try:
                    new_row = input("Введите исправленную строку:")
                    temp = main(new_row, list_oper)
                    print(temp)
                    summa += temp
                except Exception:
                    print("Неверное выражение, идем дальше")
    print("Сумма:", summa)
