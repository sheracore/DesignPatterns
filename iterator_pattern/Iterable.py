from Iterator import Iterator


class Iterable:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop()

    def iterator(self):
        return Iterator(self.items)
