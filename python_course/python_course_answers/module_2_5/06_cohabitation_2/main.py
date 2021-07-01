import random


class Home:
    """Класс дома"""
    def __init__(self):
        self.ref_food = 50
        self.money = 100
        self.food_for_cat = 30
        self.dirt = 0
        self.total_food = 0
        self.total_money = 0
        self.total_coats = 0


class Human:
    """Базовый класс человека"""

    def __init__(self, home) -> None:
        self.home = home
        self.hungry_level = 30
        self.happy_level = 100

    def pet_the_cat(self):
        """Метод 'погладить кота'"""
        self.hungry_level -= 10
        self.happy_level += 5
        return "Погладил кота"

    def live_one_day(self):
        pass


class Children(Human):
    """Класс ребенка"""

    def eat(self) -> str:
        """Метод реализующий действие 'есть' """

        number = random.randint(1, 20)
        if self.home.ref_food - number > 0:
            self.hungry_level += number
            self.home.ref_food -= number
            self.home.total_food += number
            return "Поел"
        else:
            return "Не поел"

    def walk_to_school(self):
        self.hungry_level -= 10
        return "Сходил в школу"

    def play(self) -> str:
        """Метод реализующий действие 'играть' """
        self.hungry_level -= 10
        self.happy_level += 20
        return "Поиграл в игры"

    def live_one_day(self) -> str:
        """Метод реализующий один день из жизни экземпляра """
        if home.dirt > 90:
            self.happy_level -= 10
        if self.happy_level < 10 or self.hungry_level < 0:
            return "Смерть"
        if self.hungry_level <= 19:
            return self.eat()
        elif self.happy_level <= 25:
            return self.play()
        else:
            return random.choice([self.walk_to_school(), self.pet_the_cat()])


class Adult(Human):
    """Класс взрослого"""

    def eat(self) -> str:
        """Метод реализующий действие 'есть' """
        number = random.randint(10, 30)
        if self.home.ref_food - number > 0:
            self.hungry_level += number
            self.home.ref_food -= number
            self.home.total_food += number
            return "Поел"
        else:
            return "Не поел"


class Husband(Adult):
    """Класс мужа"""

    def play(self) -> str:
        """Метод реализующий действие 'играть' """
        self.hungry_level -= 10
        self.happy_level += 20
        return "Играет"

    def walk_on_work(self) -> str:
        """Метод реализующий действие 'идти на работу' """
        self.hungry_level -= 10
        self.home.money += 150
        self.home.total_money += 150
        return "Идет на работу"

    def live_one_day(self) -> str:
        """Метод реализующий один день из жизни экземпляра """
        if home.dirt > 90:
            self.happy_level -= 10
        if self.hungry_level <= 0 or self.happy_level < 10:
            return "Смерть"
        if self.hungry_level <= 20:
            return self.eat()
        elif self.happy_level <= 20:
            return self.play()
        else:
            return random.choice([self.walk_on_work(), self.pet_the_cat()])


class Wife(Adult):
    """Класс жены"""

    def buy_food(self) -> str:
        """Метод реализующий действие 'купить еды' """
        number = random.randint(100, 120)
        if self.home.money - number > 0:
            self.home.money -= number
            self.home.ref_food += number
            return "Куплена еда"
        else:
            return "Не хватило на еду"

    def buy_food_to_cat(self) -> str:
        """Метод реализующий действие 'купить еды коту' """
        self.hungry_level -= 10
        number = random.randint(30, 60)
        if self.home.money - number > 0:

            self.home.food_for_cat += number
            return "Куплена еда для кота"
        else:

            return "Не хватило денег на еду для кота"

    def buy_coat(self) -> str:
        """Метод реализующий действие 'купить шубу' """
        if self.home.money - 350 > 0:
            self.hungry_level -= 10
            self.home.money -= 350
            self.happy_level += 60
            home.total_coats += 1
            return "Куплена шуба"
        else:
            return self.pet_the_cat()

    def clean_up_home(self) -> str:
        """Метод реализующий действие 'уборка в доме' """
        self.hungry_level -= 10
        number = random.randint(50, 100)
        self.home.dirt -= number
        return "Уборка"

    def live_one_day(self) -> str:
        """Метод реализующий один день из жизни экземпляра """
        if home.dirt > 90:
            self.happy_level -= 10
        if self.hungry_level <= 0 or self.happy_level < 10:
            return "Смерть"
        elif self.hungry_level <= 25:
            return self.eat()
        elif self.happy_level <= 10:
            return self.buy_coat()
        elif self.home.ref_food < 80 or self.home.food_for_cat < 30:
            self.hungry_level -= 10
            if self.home.ref_food < 80:
                self.buy_food()
            if self.home.food_for_cat < 30:
                self.buy_food_to_cat()
            return "сходил в магазин"
        elif self.home.dirt > 50:
            return self.clean_up_home()
        else:
            return self.pet_the_cat()


class Cat:
    """Класс кота"""

    def __init__(self, home) -> None:
        self.home = home
        self.hungry_level = 30

    def eat(self) -> str:
        """Метод реализующий действие 'Есть' """
        number = random.randint(1, 10)
        if self.home.food_for_cat - number > 0:

            self.hungry_level += number * 2
            self.home.food_for_cat -= number
            self.home.total_food += number
            return "Ест"
        else:
            return "Не поел"

    def sleep(self) -> str:
        """Метод реализующий действие 'спать' """
        self.hungry_level -= 10
        return "Спит"

    def wallpapper_tear(self) -> str:
        """Метод реализующий действие 'Драть обои' """
        self.hungry_level -= 10
        self.home.dirt += 5
        return "Дерет обои"

    def live_one_day(self) -> str:
        """Метод реализующий один день из жизни экземпляра """
        if self.hungry_level <= 0:
            return "Смерть"
        if self.hungry_level <= 20:
            return self.eat()
        else:
            return random.choice([self.wallpapper_tear(), self.sleep()])


home = Home()
cat = Cat(home)
cat2 = Cat(home)
husband = Husband(home)
wife = Wife(home)
children = Children(home)

for i in range(1, 366):
    print("День", i)
    home.dirt += 5
    result1 = cat.live_one_day()
    result2 = cat2.live_one_day()
    result3 = husband.live_one_day()
    result4 = wife.live_one_day()
    result5 = children.live_one_day()
    print(f"Кот выполняет действие {result1}")
    print(f"Второй кот выполняет действие {result2}")
    print(f"Муж выполняет действие {result3}")
    print(f"Жена выполняет действие {result4}")
    print(f"Ребенок выполняет действие {result5}")

    print("--------------------------------------------------")
    print(f"|Еда {home.ref_food}| Еда для котов {home.food_for_cat} | Деньги {home.money}| Грязь {home.dirt}|")
    print("--------------------------------------------------")
    if result1 == "Смерть" or result2 == "Смерть" or result3 == "Смерть" or result4 == "Смерть" or result5 == "Смерть":
        break

print(f"Было заработано {home.total_money}, съедено еды {home.total_food}, куплено {home.total_coats} шуб")
