def containers(containers_count):
    containers_list = []
    for container in range(1, containers_count + 1):
        container_mas = int(input("Введите вес контейнера: "))
        if container_mas <= 200:
            containers_list.append(container_mas)
        else:
            return None
    return containers_list


def add_container(containers_list):
    new_container_mas = int(input("\nВведите вес нового контейнера: "))
    count_new_container = 0
    for current_container in containers_list:
        count_new_container += 1
        if current_container >= new_container_mas > containers_list[count_new_container] or count_new_container == len(
                containers_list):
            print("Номер, куда встанет новый контейнер: ", count_new_container + 1)
            break


x = int(input("Кол-во контейнеров: "))
add_container(containers(x))
