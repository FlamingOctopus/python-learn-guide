from random import randint, choice

CARMA = 500


class KillError(Exception):
    desc = "убиты"


class DrunkError(Exception):
    desc = "спились"


class CarCrashError(Exception):
    desc = "попали в автокатастрофу"


class GluttonyError(Exception):
    desc = "умерли от обжорства"


class DepressionError(Exception):
    desc = "убиты тоской"


def one_day(day: int, total_carma: int) -> tuple:
    try:
        list_rand_choice = ['', '', '', '', '', '', '', '', '', 'exc']
        list_exc = [KillError(), GluttonyError(), DrunkError(), CarCrashError(), DepressionError()]
        total_carma += randint(1, 7)
        day += 1
        if choice(list_rand_choice) == "exc":
            raise choice(list_exc)
    except Exception as e:
        with open('karma.log', 'a') as karma_file:
            karma_file.write(f"Вы {e.desc}, начинается ваше следующее перерождение\n")
    finally:
        return day, total_carma


day = 1
total_carma = 0
while True:
    day, total_carma = one_day(day, total_carma)
    if total_carma >= CARMA:
        print(f"Вы наконец достигли просветления за {day} дней?")
        break
