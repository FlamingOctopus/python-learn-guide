print('Задача 7. Стипендия')

educational_grant = int(input("Введите степендию "))
expenses = int(input("Введите расходы "))
sum_expenses = expenses - educational_grant
for i in range(2, 11):
    print(expenses)
    expenses += (expenses * 0.03)
    sum_expenses += (expenses - educational_grant)

    print(f"Нужно попросить {sum_expenses} рублей")
