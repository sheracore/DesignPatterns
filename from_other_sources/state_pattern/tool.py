from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass
    