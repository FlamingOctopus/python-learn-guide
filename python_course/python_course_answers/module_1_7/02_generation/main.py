number = int(input("Введите длину списка: "))
my_list = [1 if number % 2 == 0 else number % 5 for number in range(0, number)]
print("Результат: ", my_list)