import math

class Circle:
    def __init__(self, X=0, Y=0, R=1):
        self.X = X
        self.Y = Y
        self.R = R

    def square(self):
        return math.pi * self.R ** 2

    def perimetr(self):
        return 2 * math.pi * self.R

    def rise(self, multi):
        self.R *= multi

    def crossing(self, obj_circle):
        if isinstance(obj_circle, Circle):
            d = math.sqrt(((self.X - obj_circle.X) ** 2) + ((self.Y - obj_circle.Y) ** 2))
            if d > obj_circle.R + self.R:
                return "Окружности не пересекаются"
            else:
                return "Окружности пересекаются"

circle1 = Circle()
circle2 = Circle(4, 4, 1)
print(circle1.crossing(circle2))
circle3 = Circle()
circle4 = Circle(2, 2, 2)
print(circle3.crossing(circle4))