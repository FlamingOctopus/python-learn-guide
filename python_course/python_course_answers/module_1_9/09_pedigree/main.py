def persons_wood(persons_current):
    persons_dict = dict()
    temp_current = 0
    for person in range(1,persons_current):
        person_list = input(f"{person} пара: ").split()
        if person_list[1] in persons_dict:
            persons_dict[person_list[0]] = persons_dict[person_list[1]] + 1
        else:
            persons_dict[person_list[1]] = temp_current
            persons_dict[person_list[0]] = persons_dict[person_list[1]] + 1
            temp_current = 1
    sort_persons(persons_dict)

def sort_persons(persons_dict):
    sorted_dict = {}
    sorted_keys = sorted(persons_dict)
    print('“Высота” каждого члена семьи:')
    for values in sorted_keys:
        sorted_dict[values] = persons_dict[values]
    for values in sorted_dict.items():
        print("\t", values[0], values[1])

persons_current = int(input("Введите количество человек: "))
persons_wood(persons_current)