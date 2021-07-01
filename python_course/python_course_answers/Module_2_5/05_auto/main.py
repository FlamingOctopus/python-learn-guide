class Car:
    def __init__(self, coord_x: int, coord_y: int, angle: int) -> None:
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__angle = angle % 360

    def move(self, distance):
        self.distance = distance

    def change_angle(self, angle):
        self.__angle = angle % 360


class Bus(Car):
    def __init__(self, coord_x: int, coord_y: int, angle: int) -> None:
        super().__init__(coord_x, coord_y, angle)
        self.__passengers = 0
        self.__money = 0
        self.__tax = 2

    def move(self, distance):
        self.__money += self.__passengers * self.__tax * distance

    def add_passengers(self, count):
        self.__passengers += count

    def reduce_passengers(self, count):
        if self.__passengers - count < 0:
            raise Exception
        self.__passengers -= count

    def __str__(self):
        return f"Автобус едет с {self.__passengers} пассажирами, заработал {self.__money}"


car = Car(0, 0, 120)
bus = Bus(0, 0, 180)

bus.move(10)
print(bus)
bus.change_angle(120)
bus.add_passengers(10)
bus.move(100)
print(bus)
bus.move(100)
print(bus)
bus.reduce_passengers(5)
bus.move(100)
print(bus)
