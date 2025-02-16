
from typing import List, Iterator

# Iterator Interface
class NameIterator(Iterator):
    def __init__(self, names: List[str]):
        self._names = names
        self._index = 0

    def __next__(self):
        if self._index >= len(self._names):
            raise StopIteration  # End of collection
        value = self._names[self._index]
        self._index += 1
        return value

# Iterable (Collection)
class NameCollection:
    def __init__(self, names: List[str]):
        self._names = names

    def __iter__(self):
        return NameIterator(self._names)

# Client Code
if __name__ == "__main__":
    names = NameCollection(["Alice", "Bob", "Charlie"])

    for name in names:
        print(name)

# Output:
# Alice
# Bob
# Charlie



# Python’s Built-in Iterator Support
def name_generator(names):
    for name in names:
        yield name  # Returns each name lazily

names = ["Alice", "Bob", "Charlie"]
for name in name_generator(names):
    print(name)
