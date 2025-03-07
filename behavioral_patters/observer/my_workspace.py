class Event(list):
    def __call__(self, *args, **kwargs):
        for event in self:
            event(*args, **kwargs)


class Member:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        return f"{self.username} with level: {self.level}"

class Apex:
    def __init__(self):
        self.events = Event()

    def join(self, memeber):
        self.events(memeber)


class GameServer:
    def __init__(self, apex):
        self.apex = apex
        self.apex.events.append(self.join)
        self.apex.events.append(self.income)

    def join(self, member):
        print(f"Joining {member.username}")

    def income(self, member):
        print(f"income of {member.username} is ${len(member.username)*9000} in a year")



if __name__ == "__main__":
    m1 = Member('Sheracore123', 'Diamonds')
    m2 = Member('Sher', 'Legends')
    apex = Apex()
    GameServer(apex)
    apex.join(m1)
    apex.join(m2)
