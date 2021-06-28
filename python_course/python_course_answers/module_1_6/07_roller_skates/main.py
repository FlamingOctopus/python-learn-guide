def skates_list_generate():
    N = int(input("Кол-во коньков: "))
    skates_list = []
    for skates in range(1, N + 1):
        size = int(input(f"Размер {skates} пары: "))
        count = 0
        for boots in skates_list:
            if boots[0] == size:
                boots[1] += 1
            elif count == skates:
                skates_list.append([size, 1])
        else:
            skates_list.append([size, 1])
    return skates_list


def people_skates(skates_list):
    N = int(input("Кол-во людей: "))
    count_people = 0
    for people in range(1, N + 1):
        size_people = int(input(f"Размер ноги  {people} человека:  "))
        for boots_people in skates_list:
            if boots_people[0] == size_people and boots_people[1] > 0:
                count_people += 1
                boots_people[1] -= 1
                break
            elif boots_people[0] > size_people and boots_people[1] > 0:
                count_people += 1
                boots_people[1] -= 1
                break
    return count_people


print("Наибольшее кол-во людей, которые могут взять ролики: ", people_skates(skates_list_generate()))
