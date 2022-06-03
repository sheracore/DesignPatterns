from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declare a method for executing a command
    """

    @abstractmethod
    def execute(self) -> None:
        pass
