from abc import abstractmethod


class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.__age = age


class Employee(Person):

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):
    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__(name, surname, age)
        self.salary()

    def salary(self) -> None:
        self.__salary = 13000

    def get_salary(self) -> int:
        return self.__salary


class Agent(Employee):
    def __init__(self, name: str, surname: str, age: int, sells: int) -> None:
        super().__init__(name, surname, age)
        self.__sells = sells
        self.salary()

    def salary(self) -> None:
        self.__salary = 5000 + (self.__sells * 0.05)

    def get_salary(self) -> float:
        return self.__salary


class Worker(Employee):
    def __init__(self, name: str, surname: str, age: int, hours: int) -> None:
        super().__init__(name, surname, age)
        self.__hours = hours
        self.salary()

    def salary(self) -> None:
        self.__salary = 100 * self.__hours

    def get_salary(self) -> int:
        return self.__salary


manager1 = Manager("Jack", "White", 29)
manager2 = Manager("Mike", "Black", 31)
manager3 = Manager("Nik", "Brown", 44)

agent1 = Agent("Beck", "Orange", 34, 100)
agent2 = Agent("Ivan", "Smith", 23, 90)
agent3 = Agent("Nik", "Strovsky", 29, 95)

worker1 = Worker("Max", "Blue", 30, 120)
worker2 = Worker("Kris", "Kross", 50, 130)
worker3 = Worker("John", "John", 25, 125)

list_persons = [manager1, manager2, manager3, agent1, agent2, agent3, worker1, worker2, worker3]

for person in list_persons:
    print(f"{person.name} {person.surname} earn {person.get_salary()}")
