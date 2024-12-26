class GroupClass:
    def __init__(self, name):
        self._name = name
        self.children = []

    @property
    def name(self):
        return self._name

    def __str__(self):
        items = []
        self._collect(items)
        return ", ".join(items)
        # for child in self.children:
        #     print(child.name)

    def _collect(self, items):
        items.append(self.name)
        for child in self.children:
            self._collect(child)



class Apple:
    def __init__(self, taste):
        self.taste = taste


    @property
    def name(self):
        return self.taste



class Device:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color


    @property
    def name(self):
        return self.shape + "===" + self.color


if __name__ == "__main__":
    group_A = GroupClass('A')
    a1 = Apple('sweet')
    a2 = Apple('bitter')
    group_A.children.append(a1)
    group_A.children.append(a2)
    d1 = Device('large', 'black')
    d2 = Device('small', 'orange')
    group_B = GroupClass('B')
    group_B.children.append(d1)
    group_B.children.append(d2)
    group_B.children.append(group_A)
    print(group_B)
