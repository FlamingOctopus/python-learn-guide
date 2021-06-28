def div_num(number):
    if number > 1:
        for current_div in range(2, number + 1):
            if (number / current_div) % 1 == 0:
                return current_div
    else:
        return "Ошибка: число меньше или равно 1"


n = int(input("Введите число: "))
print(f"Наименьший делитель, отличный от единицы: {div_num(n)}")
