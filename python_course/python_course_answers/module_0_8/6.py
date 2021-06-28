print('Задача 6. Письмо')

a = int(input('Введите размер : '))
a = (a + 11) // 12
count = 0
j = 1
for i in range(a) :
  if j > a - 1 :
      break
  j *= 2
  count += 2
print(f"Нужно сложить {count} раза")

