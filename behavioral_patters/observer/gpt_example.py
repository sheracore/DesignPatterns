from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received update: {message}")


# Subject (Observable)
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# Example Usage
subject = Subject()

# Create observers
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

# Register observers
subject.add_observer(observer1)
subject.add_observer(observer2)

# Notify observers of a state change
subject.notify_observers("New event has occurred!")

# Remove an observer and notify again
subject.remove_observer(observer1)
subject.notify_observers("Another event update!")

