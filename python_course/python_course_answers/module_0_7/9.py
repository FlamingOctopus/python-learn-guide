print('Задача 9. ...Теперь можно посчитать и свою')

flag = False

for i in range(1, 13):
    x = int(input(f"Введите зарплату за {i} месяц"))
    if i == 1:
        past_x = x
        continue
    elif past_x >= x:
        flag = True
        break
    else:
        past_x = x
        continue

if flag == True:
    print("ЗП не растет равновмерно")
else:
    print("ЗП растет равновмерно")