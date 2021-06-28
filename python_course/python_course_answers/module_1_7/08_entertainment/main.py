branch_count, drop_count = int(input("Кол-во палок:")), int(input("Кол-во бросков:"))
row = ['I'] * branch_count
for drop in range(drop_count):
    left, right = int(input(f"Бросок {drop + 1}. Сбиты палки с номера ")), int(input(f"по номер "))
    for branch in range(left - 1, right):
        row[branch] = '.'
print("Результат: ", ''.join(row))