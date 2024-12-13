class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self, x):
        self.x = x
        print("Loading database...")


d1 = Database(1)
d2 = Database(2)

print(d1 == d2)
print(d1.x, d2.x)