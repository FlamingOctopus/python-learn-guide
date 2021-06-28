print('Задача 3. Число наоборот 2')


def reverseNum(x):
  rev_num = ""
  for i in x:
    rev_num = i+rev_num
  return rev_num

a = input("Введите первое число:")
b = input("Введите второе число:")

print(f"Первое число наоборот:{reverseNum(a)}\nВторое число наоборот: {reverseNum(b)}")
print(f"Сумма: {int(reverseNum(a))+int(reverseNum(b))}\nСумма наоборот: {reverseNum(str(int(reverseNum(a))+int(reverseNum(b))))}")