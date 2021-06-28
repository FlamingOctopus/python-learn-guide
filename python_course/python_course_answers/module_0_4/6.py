print('Задача 6. Игра в кубики')

kostia_count = int(input("Кубик Кости:"))
owner_count = int(input("Кубик владельца:"))

if kostia_count >= owner_count:
  print(f'Сумма: {kostia_count-owner_count} \nКостя платит')
else:
    print(f'Сумма: {owner_count-kostia_count} \nВладелец платит платит')

print("Игра окончена")