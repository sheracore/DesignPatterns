from enum import Enum
from math import *

class Point:

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))



if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point.new_cartesian_point(1, 2)
    p3 = Point.new_polar_point(5, 6)
    print(p1, p2, p3)