class Parent:
    def __init__(self, name, age, *childrens):
        self.name = name
        self.age = age
        self.childrens = childrens
        for children in self.childrens:
            if self.age - children.age <= 16:
                raise Exception("Возрастная разница слишком маленькая")

    def __str__(self):
        return f"Я {self.name}, мне {self.age}, мои дети: {','.join(list(children.name for children in self.childrens))}"

    def relax(self, name):
        for children in self.childrens:
            if children.name == name:
                if children.mood:
                    children.mood = False
                    print(f"{children.name} успокоился")
                else:
                    print(f"{children.name} спокоен")

    def feed(self, name):
        for children in self.childrens:
            if children.name == name:
                if children.hungry:
                    children.hungry = False
                    print(f"{children.name} накормлен")
                else:
                    print(f"{children.name} не голоден")

class Children:
    mood = True
    hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

child1 = Children("Вася", 2)
child2 = Children("Аня", 3)
parent1 = Parent("Иван", 40, child1,child2)

print(parent1)
parent1.feed("Вася")
parent1.feed("Вася")
parent1.relax("Вася")
parent1.relax("Вася")