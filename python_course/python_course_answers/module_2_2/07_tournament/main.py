from collections import OrderedDict

with open('first_tour.txt', 'r') as file:
    rows = file.readlines()
    peoples_dict = {}
    print("Содержимое файла first_tour.txt:")
    for row in rows:
        print(row, end = '')
        new_row = row.replace("\n", "").split(' ')
        if len(new_row) == 1:
            K = int(row)
            continue
        key = f"{new_row[1][0]}. {new_row[0]}"
        peoples_dict[key] = int(new_row[2])

new_dict = OrderedDict(sorted(peoples_dict.items(), key=(lambda x: x[1])))

list_peoples = []
for id, (item, value) in (enumerate(reversed(new_dict.items()), 1)):
    if K < value:
        count = str(id)
        list_peoples.append(f"{id}) {item} {value}")

f = open("second_tour.txt", 'w')
f.write(count)
f.write('\n')
f.write("\n".join(list_peoples))
f.close()

f = open("second_tour.txt", 'r')
rows = f.readlines()
print("\n\nСодержимое файла second_tour.txt:")
for row in rows:
    print(row, end = '')
f.close()
