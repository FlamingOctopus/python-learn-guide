students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


for id, student in students.items():
    print(id, "-", student['age'])


def students_interest_and_len_surname(students_dict):
    """Эта функция выводит все интересы студентов и общую длину их фамилий"""
    interests_list = list()
    total_len_surnames = 0
    for student in students_dict:
        interests_list.append(students_dict[student]['interests'])
        total_len_surnames += len(students_dict[student]['surname'])
    return interests_list, total_len_surnames


interests, lenth_surnames = students_interest_and_len_surname(students)

print(f"Интересы студентов:{interests} \nОбщая длина фамилий: {lenth_surnames}")
