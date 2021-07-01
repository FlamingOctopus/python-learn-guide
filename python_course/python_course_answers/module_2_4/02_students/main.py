class Student:
    def __init__(self, name, group_number,rating):
        self.name = name
        self.group_number = group_number
        self.rating = rating

student1 = Student("Николай Иванов",1,3.2)
student2 = Student("Иван Иванов",1,3.5)
student3 = Student("Иван Николаев",1,3.2)
student4 = Student("Сергей Иванов",1,3.9)
student5 = Student("Владимир Иванов",1,4.0)

sorted_list = sorted([student1,student2,student3,student4,student5], key = lambda x: x.rating )
print([i.name for i in sorted_list])