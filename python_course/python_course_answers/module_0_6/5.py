print('Задача 5. Счастливый билетик')

number = int(input("Число:"))
left, right, sum1, sum2 = 0, 0, 0, 0

while number > 999:
    left = number % 10
    number //= 10
    sum1 += left

while int(number) != 0:
    right = number % 10
    number //= 10
    sum2 += right

if sum1 == sum2:
    print("Счастливый")
else:
    print("Не счастливый")
# Подумайте, нужны ли для решения этой задачи циклы?
# Не нужны, т.к. тут определенная длина числа.