def func(first_cord_pos, second_cord_pos, radius):
    if first_cord_pos ** 2 + second_cord_pos ** 2 <= radius ** 2:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


print("Введите координаты монетки: ")
x, y = float(input("X: ")), float(input("Y: "))
r = int(input("Введите радиус: "))
func(x, y, r)
