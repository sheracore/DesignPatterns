from collections import deque


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

    def get_urls(self):
        return self._urls
