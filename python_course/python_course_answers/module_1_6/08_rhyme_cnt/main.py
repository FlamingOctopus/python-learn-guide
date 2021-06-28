def counter(people_count, number):
    list_people = [people for people in range(1, people_count + 1)]
    current_element = 0
    while len(list_people) != 1:
        print("Текущий круг людей:", list_people, \
              "\nНачало счёта с номера ", list_people[current_element])
        current_element = (current_element + number) % len(list_people) - 1
        print("Выбывает человек под номером ", list_people[current_element], '\n')
        list_people.remove(list_people[current_element])
        if list_people[current_element] == list_people[-1]:
            current_element = 0
    print("Остался человек под номером ", list_people[0])


x, y = int(input("Кол-во человек: ")), int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {y} человек")
counter(x, y)
