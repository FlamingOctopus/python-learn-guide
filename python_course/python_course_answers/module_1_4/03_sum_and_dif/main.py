def sum_num(number):
    numbers_sum = 0
    for i in str(number):
        numbers_sum += int(i)
    return numbers_sum


def kol_num(number):
    quantity = 0
    for i in str(number):
        quantity += 1
    return quantity


N = int(input("Введите число: "))
summa = sum_num(N)
kol = kol_num(N)

print(f"Сумма цифр: {summa}\n\
        Кол-во цифр в числе:{kol}\n\
        Разность суммы и кол-ва цифр: {summa - kol}")
