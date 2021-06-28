print('Задача 3. Это будет бомба')

N = int(input("Введите время "))

for i in range(N, -1, -1):
    if i == 0:
        print("Бомба взорвалась!")
        break
    x = int(input("Хотите обезвредить сейчас? "))
    if x == 0:
        continue
    else:
        print("Бомба обезвреженна")
        break

