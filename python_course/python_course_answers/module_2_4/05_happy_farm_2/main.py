class Potato:
    def __init__(self, number):
        self.number = number
        self.grow = 0

    def growing(self):
        if self.grow < 5:
            self.grow += 1
            self.info_growing()

    def info_growing(self):
        print(f"Картошка номер {self.number} имеет стадию зрелости - {self.grow}")

    def Is_grow(self):
        if self.grow == 4:
            return True
        return False

class Garden:
    def __init__(self, count):
        self.potatoes = [Potato(number) for number in range(1, count + 1)]

    def growing_garden(self):
        print("Картошка растет")
        for potato in self.potatoes:
            potato.growing()

    def growed_val(self):
        if all([potato.Is_grow for potato in self.potatoes]):
            print("Картошка созрела")
            return True
        return False

class Gardener:
    def __init__(self, name, obj_garden):
        self.name = name
        self.garden = obj_garden
        self.fruit = []

    def care(self):
        while True:
            print("Ухаживаем за растениями")
            self.garden.growing_garden()
            if self.garden.growed_val():
                print("Собираем урожай")
                self.collect()
                break

    def collect(self):
        print("Урожай собран")
        self.garden.potatoes = []

garden1 = Garden(5)
gard_worker = Gardener("Вася",garden1)
gard_worker.care()
gard_worker.care()
gard_worker.care()
gard_worker.care()