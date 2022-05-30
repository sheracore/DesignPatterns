from collections import deque
from Iterator import Iterator


class BrowserHistory:
    def __init__(self):
        self._urls = deque()

    @property
    def get_urls(self):
        return self._urls

    def pop(self):
        try:
            self._urls.pop()
        except IndexError:
            print("ERROR! history is empty")

    def push(self, url):
        self._urls.push(url)

    def create_iterator(self):
        from
        return ListIterator(self);

    class ListIterator(Iterator):
        def __init__(self):
            self._history = BrowserHistory()
            self._index = int()

        def has_next(self):
            return self._index < len(self._history._urls)

        def current(self):
            return self._history._urls(self._index)

        def next(self):
            self._index += 1

