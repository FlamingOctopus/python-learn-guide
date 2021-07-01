import random


class Home:
    ref_eat = 50
    money = 0


class Person:
    count = 0

    def __init__(self, name, obj_home):
        self.name = name
        self.home = obj_home
        self.hungry = 50

    def eat(self) -> str:
        self.hungry += 20
        self.home.ref_eat -= 20
        return "Время перекусить"

    def work(self) -> str:
        self.hungry -= 20
        self.home.money += 20
        return "Идем на работу"

    def play(self) -> str:
        self.hungry -= 20
        return "Можно поиграть"

    def buy_food(self) -> str:
        self.home.money -= 20
        self.home.ref_eat += 20
        return "Идем в магазин за едой"

    def live_one_day(self) -> str:
        rand = random.randint(1, 6)
        if self.hungry < 0:
            return "Смерть"
        if self.hungry < 20:
            status = self.eat()
        if self.home.ref_eat < 10:
            status = self.buy_food()
        elif self.home.money < 50:
            status = self.work()
        elif rand == 1:
            status = self.work()
        elif rand == 2:
            status = self.eat()
        else:
            status = self.play()
        return status


home = Home()
people = Person("Mike", home)
people2 = Person("Nik", home)

for i in range(1, 366):
    print("День", i)
    result1 = people.live_one_day()
    result2 = people2.live_one_day()
    if result1 == "Смерть" or result2 == "Смерть":
        break
    print(f"{people.name} выполняет действие {result1}")
    print(f"{people2.name} выполняет действие {result2}")
