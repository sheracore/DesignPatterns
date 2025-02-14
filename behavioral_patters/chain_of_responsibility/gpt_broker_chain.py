class Event:
    def __init__(self, name, data):
        self.name = name
        self.data = data

class EventBroker:
    def __init__(self):
        self.subscribers = []  # List of handlers

    def subscribe(self, handler):
        self.subscribers.append(handler)

    def publish(self, event):
        for subscriber in self.subscribers:
            subscriber.handle(event)  # Each handler processes the event

class Handler:
    def __init__(self, name):
        self.name = name

    def handle(self, event):
        print(f"{self.name} received event: {event.name} with data {event.data}")

# Create broker (chain)
broker = EventBroker()

# Create handlers
handler1 = Handler("Handler 1")
handler2 = Handler("Handler 2")

# Subscribe handlers to the broker
broker.subscribe(handler1)
broker.subscribe(handler2)

# Publish an event (both handlers receive it)
broker.publish(Event("UserSignedUp", {"username": "john_doe"}))