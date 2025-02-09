from abc import ABC, abstractmethod


class Bird:
    def fly(self):
        return "I can fly!"

class Sparrow(Bird):
    pass


# Usage
def make_it_fly(bird: Bird):
    print(bird.fly())

sparrow = Sparrow()
make_it_fly(sparrow)  # Works as Sparrow follows the behavior of Bird


class Bird:
    def fly(self):
        return "I can fly!"

class Ostrich(Bird):  # Ostrich cannot fly
    def fly(self):
        return "I can't fly!"

# Usage
def make_it_fly(bird: Bird):
    print(bird.fly())

ostrich = Ostrich()
make_it_fly(ostrich)  # Violates LSP: Ostrich does not behave like a Bird


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        return "I can fly!"

class NonFlyingBird(Bird):
    def fly(self):
        return "I can't fly!"

class Sparrow(FlyingBird):
    pass

class Ostrich(NonFlyingBird):
    pass


# Usage
def make_it_fly(bird: FlyingBird):
    print(bird.fly())

sparrow = Sparrow()
make_it_fly(sparrow)  # Works
# make_it_fly(Ostrich())  # Would raise a type error now


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


# This class will break the liskov principle
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)