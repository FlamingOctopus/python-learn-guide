print('Задача 5. Факториал')
num = 1
N = int(input("Введите число "))
for i in range(1, N + 1):
    num = num * i
    print(num)

print(f"Факториал {N} число {num}")