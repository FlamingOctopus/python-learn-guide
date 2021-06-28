def list_creator(end_number):
    list_numbers = []
    for current_number in range(1, end_number + 1):
        if current_number % 2 > 0:
            list_numbers.append(current_number)
    return list_numbers


N = int(input("Введите число: "))
print("Список нечетных чисел: ", list_creator(N))
