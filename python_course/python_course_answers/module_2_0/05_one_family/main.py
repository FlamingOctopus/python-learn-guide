# families = {
#     ("Сидоров", 'Сидорова'): {('Сидоров', 'Никита'): 35, ('Сидорова', 'Алина'): 35,('Сидоров', 'Павел'): 35},
#
#     ("Петров", "Петрова"): {('Петров', 'Никита'): 35, }
# }
#
# surname = input("Введите фамилию: ").title()
# for person_wrap, people in families.items():
#     if surname in person_wrap:
#         for person,age in people.items():
#             print(person[0], person[1], age)

families = {
   'Сидоров Никита': 35, 'Сидорова Алина': 35,'Сидоров Павел': 35, 'Петров Никита': 35,
}

surname = input("Введите фамилию: ").title()
for person_wrap, people in families.items():
    if (surname and surname[:-1]) in person_wrap:
        print(person_wrap, people)