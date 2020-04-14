import math
pi = math.pi


class Shape:
    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.r = radius

    def cal_area(self):
        return pi * self.r**2

    def cal_perimeter(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.w = width
        self.h = height

    def cal_area(self):
        return self.w * self.h

    def cal_perimeter(self):
        return 2 * (self.w + self.h)


c1 = Circle(10)
print(c1.cal_area())
print(c1.cal_perimeter())
print(c1.get_color())
c1.set_color('white')
print(c1.get_color())

print('============')

r1 = Rectangle(2, 5)
print(r1.cal_area())
print(r1.cal_perimeter())
print(r1.get_color())
r1.set_color('yellow')
print(r1.get_color())
