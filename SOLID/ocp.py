from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods


# Enterprise Patterns: Specification


class Specification:
    def is_satisfied(self, item):
        pass


class Filter:
    def filter(self, item, spec: Specification):
        pass


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return self.size == item.size


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return self.color == item.color


class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, item_list, spec):
        for item in item_list:
            if spec.is_satisfied(item):
                yield item


bf = BetterFilter()

apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)
products = [apple, tree, house]

size_large = SizeSpecification(Size.LARGE)

for p in bf.filter(products, size_large):
    print(p.name, "is large")

size_large = SizeSpecification(Size.LARGE)
color_green = ColorSpecification(Color.GREEN)

green_large = AndSpecification(size_large, color_green)

for p in bf.filter(products, green_large):
    print(p.name, "size: ",  p.size, "color: ", p.color, " combination")
