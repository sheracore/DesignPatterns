import random

class Database:
    _instance = None

    def __init__(self):
        self.id = random.randint(1,101)
        print('Generated an id of ', self.id)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls) \
                .__new__(cls, *args, **kwargs)

        return cls._instance



if __name__ == '__main__':
    d0 = Database()
    print(d0.id)
    d1 = Database()
    print(d1.id)
    d2 = Database()

    print(d0.id, d1.id, d2.id)
    print(d1 == d2)
    print(d0 == d1)