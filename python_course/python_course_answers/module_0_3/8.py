print('Задача 8. Режем число на части')
number = int(input("Введите четырехзначное число: "))
print(number//1000, ((number//100)%10),((number//10)%10),number%10)