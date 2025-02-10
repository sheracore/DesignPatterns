from collections import deque


class History:
    def __init__(self):
        self._editor_state_list = deque()

    def push(self, state):
        self._editor_state_list.append(state)

    def pop(self):
        try:
            return self._editor_state_list.pop()
        except IndexError:
            print("It's not any state to restore")
