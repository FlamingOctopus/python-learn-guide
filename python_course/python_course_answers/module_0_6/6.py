print('Задача 6. Поставьте оценку!')

x = int
count_pol, count_neg = 0, 0
while x != 0:
    x = int(input("Введите оценку "))
    if x > 0:
        count_pol += 1

    elif x < 0:
        count_neg += 1

print("Положительных оценок:", count_pol)
print("Негативных оценок:", count_neg)