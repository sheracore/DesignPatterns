class A:
    def __init__(self):
        self.name = 'Hassan'

    def show_name(self):
        print(self.name)


class B:
    def __init__(self, a : A):
        self._a = a
        self._a.name = 'Mohsen'


if __name__ == '__main__':
    a = A()
    a.show_name()
    B(a)
    a.show_name()
