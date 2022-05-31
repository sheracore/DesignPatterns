from Item import Item
from Iterable import Iterable

if __name__ == '__main__':
    i1 = Item("Burger", 7)
    i2 = Item("Pizza", 8)
    i3 = Item("Coke", 5)

    menu = Iterable()
    menu.add(i1)
    menu.add(i2)
    menu.add(i3)

    iterator = menu.iterator()
    while iterator.has_next():
        item = iterator.next()
        print(item)
