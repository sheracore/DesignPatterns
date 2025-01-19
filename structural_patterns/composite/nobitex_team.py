class Team:
    def __init__(self, name):
        self._name = name
        self.children = []

    @property
    def name(self):
        return self._name

    def display(self, items, depth=0):
        items.append("\t"*depth + f"{self.name}\n")
        for child in self.children:
            child.display(items, depth+1)

    def __str__(self):
        items = []
        self.display(items)
        return ", ".join(items)


if __name__ == "__main__":
    nobitex_teams = Team('Nobitex teams')
    labs = Team('lobi labs')
    ios = Team('iso')
    android = Team('android')
    blockchain = Team('blockchain')
    blockchain.children.append(Team('hot cold'))
    blockchain.children.append(Team('core blockchain'))
    blockchain.children.append(Team('explorer'))
    nobitex_teams.children.append(labs)
    nobitex_teams.children.append(ios)
    nobitex_teams.children.append(android)
    nobitex_teams.children.append(blockchain)
    print(nobitex_teams)
