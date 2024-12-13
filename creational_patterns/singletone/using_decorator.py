
"""
This decorator is one of the best approaches:

Advantages
Simple Implementation: Easy to use and understand.
Thread Safety: This implementation can be extended with locks for use in multi-threaded environments.

Disadvantages
Harder to Test: Singleton classes can make unit testing more complex because their state persists between tests unless explicitly reset.
"""

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Database:

    def __init__(self, a):
        self.a = a
        print("Loading database")


d1 = Database(4)
d2 = Database(6)
d3 = Database(11)
print(d1.a, d2.a, d3.a)

print(d1 == d2 == d3)