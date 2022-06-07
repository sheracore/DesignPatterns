from baseComponent import BaseComponent
from mediator import Mediator

"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A. ")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B. ")
        self.mediator.notify(self, "B")
