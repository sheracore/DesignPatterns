class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message, sender)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message, sender):
        print(f"{self.name} receives from {sender.name}: {message}")

# Usage
mediator = ChatMediator()
alice = User("Alice", mediator)
bob = User("Bob", mediator)

alice.send("Hello, Bob!")
bob.send("Hey, Alice!")