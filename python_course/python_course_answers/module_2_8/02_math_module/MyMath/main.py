import math


class MyMath:
    @classmethod
    def circle_len(cls, radius):
        circle_len = 2 * math.pi * radius
        return circle_len

    @classmethod
    def circle_sq(cls, radius):
        circle_sq = math.pi * (radius ** 2)
        return circle_sq

    @classmethod
    def cube_volume(cls, height):
        cube_volume = height ** 3
        return cube_volume

    @classmethod
    def sphere_sq(cls, radius):
        sphere_sq = 4 * math.pi * radius
        return sphere_sq
