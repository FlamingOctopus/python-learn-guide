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


list_oper = ['+', "-", "*", "/", "//", "%"]
summa = 0
with open("calc.txt", 'r') as file_calc:
    for row in file_calc:
        try:
            valid = validator(row, list_oper)
            first_num, oper, second_num = valid[1]
            temp = calc(first_num, oper, second_num)
            print(temp)
            summa += temp
        except Exception as exp:
            print(f"{row} - !!!  {exp} ")
    print("Сумма:", summa)
