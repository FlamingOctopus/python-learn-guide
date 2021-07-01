from abc import ABC

class Property(ABC):
    """Базовый класс для вычисления налога"""

    def __init__(self, __tax) -> None:
        self.__tax = __tax

    def interface(self) -> None:
        """Метод-интерфейс"""
        money = int(input("Введите ваш баланс: "))
        cost = int(input("Введите стоимость имущества: "))
        self.setattr(money, cost)

    def setattr(self, money: int, cost: int) -> None:
        self.__money = money
        self.__worth = cost
        self.__total_tax = self.__tax * self.__worth

    def getattr(self) -> tuple:
        """Функция возвращает кортеж
        (налог,сколько нехватает), если денег достаточно для оплаты налога,
        (налог,0)"""
        if self.__total_tax > self.__money:
            return (self.__total_tax, -(self.__total_tax - self.__money))
        else:
            return (self.__total_tax, 0)


class Apartment(Property):
    def __init__(self):
        self.__tax = 1 / 1000
        super().__init__(self.__tax)


class Car(Property):
    def __init__(self):
        self.__tax = 1 / 200
        super().__init__(self.__tax)


class CountryHouse(Property):
    def __init__(self):
        self.__tax = 1 / 500
        super().__init__(self.__tax)


apart = Apartment()
apart.interface()
print(apart.getattr())
