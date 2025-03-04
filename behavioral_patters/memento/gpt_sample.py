class Memento:
    """Stores the state of the Originator."""
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    """Creates and restores memento objects."""
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state

    def save_to_memento(self):
        print("Saving state to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Restoring state from Memento: {self._state}")


class Caretaker:
    """Manages saved states (mementos)."""
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


# Example Usage
originator = Originator("State1")
caretaker = Caretaker()

# Save states
caretaker.add_memento(originator.save_to_memento())
originator.set_state("State2")
caretaker.add_memento(originator.save_to_memento())
originator.set_state("State3")

# Restore previous states
originator.restore_from_memento(caretaker.get_memento(0))  # Restores "State1"
originator.restore_from_memento(caretaker.get_memento(1))  # Restores "State2"

