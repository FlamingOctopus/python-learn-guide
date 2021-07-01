from typing import Union
from math import sqrt


class Square:

    def __init__(self, base: Union[float, int]) -> None:
        self._base = base

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, base: float) -> None:
        self._base = base

    def s(self) -> float:
        return self._base ** 2

    def p(self) -> float:
        return self._base * 4


class Triangle:
    def __init__(self, side: Union[float, int], height: Union[float, int]) -> None:
        self._side = side
        self._height = height

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, side: float) -> None:
        self._side = side

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height

    def s(self) -> float:
        return .5 * self._height * self._side

    def p(self) -> float:
        return self._side + 2 * sqrt(self._height ** 2 + (self._side / 2) ** 2)


class Mixin:

    def s_mixin(self) -> float:
        s = 0
        for elem in self._sides:
            s += elem.s()
        return s


class Cube(Square, Mixin):
    def __init__(self, side: Union[float, int]) -> None:
        super().__init__(side)
        self._sides = [Square(side), Square(side), Square(side), Square(side), Square(side), Square(side)]


class Pyramid(Triangle, Square, Mixin):

    def __init__(self, side: Union[float, int], height: Union[float, int]) -> None:
        super().__init__(side, height)
        self._sides = [Triangle(side, height), Triangle(side, height), Triangle(side, height),
                       Triangle(side, height), Square(side)]


cube = Cube(3)
print(cube.s_mixin())

pyramid = Pyramid(3, 6)
print(pyramid.s_mixin())
