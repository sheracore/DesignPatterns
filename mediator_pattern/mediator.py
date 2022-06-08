from abc import ABC


class Mediator(ABC):
    """
    The mediator interface declares a method used by components to notify
    the mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        print("I'm in the abc mediator")
        pass
