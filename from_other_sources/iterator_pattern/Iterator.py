class Iterator:
    def __init__(self, items):
        self.indx = 0
        self.items = items

    def has_next(self):
        return False if self.indx >= len(self.items) else True

    def next(self):
        item = self.items[self.indx]
        self.indx += 1
        return item
