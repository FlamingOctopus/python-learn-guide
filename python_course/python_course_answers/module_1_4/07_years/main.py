def func(start_year, end_year):
    while start_year < end_year:
        for i in range(10):
            count_repear_nums = 0
            for number in str(start_year):
                if number == str(i):
                    count_repear_nums += 1
            if count_repear_nums == 3:
                print(start_year)
        start_year += 1


a = int(input("Введите первый год:  "))
b = int(input("Введите второй год: "))
print("Года от 1900 до 2100 с тремя одинаковыми цифрами:")
func(a, b)
