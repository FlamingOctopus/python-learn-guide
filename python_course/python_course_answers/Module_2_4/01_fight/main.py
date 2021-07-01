import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, target):
        target.resist()
        print(f"{self.name} атаковал {target.name}, у него осталось {target.health} здоровья")

    def resist(self):
        self.health -= 20



warrior_1 = Warrior("Воин1")
warrior_2 = Warrior("Воин2")

list_warriors = [warrior_1, warrior_2]

while True:
    target = random.choice(list_warriors)
    target.health -= 20
    if target == warrior_1:
        warrior_1.attack(warrior_2)
    else:
        warrior_2.attack(warrior_1)
    if target.health <= 0:
        if target == warrior_1:
            print(f"{warrior_2.name} побеждает!")
            break
        else:
            print(f"{warrior_1.name} побеждает!")
            break
