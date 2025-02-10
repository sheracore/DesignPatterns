import string
import random


class User:
    """
    User without optimization techniques
    This class  Occupies 10000 space
    """
    def __init__(self, name):
        self.name = name

class UserFlyweight:
    """
    A flyweight of a user
    This class Occupies maximum 200 space
    """
    name_list = list()

    def __init__(self, full_name):
        name, family = full_name.split(' ')
        self.name_inx = self.name_family_index(name)
        self.family_inx = self.name_family_index(family)

    def __str__(self):
        return f"{self.name_list[self.name_inx]} {self.name_list[self.family_inx]}"

    def name_family_index(self, name):
        try:
            return self.name_list.index(name)
        except ValueError:
            self.name_list.append(name)
        return len(self.name_list) - 1


chars = string.ascii_lowercase
def random_name():
    return ''.join([random.choice(chars) for _ in range(5)])

if __name__ == '__main__':
    names = [random_name() for _ in range(100)]
    families = [random_name() for _ in range(100)]


    """
    Players insert full names 
    but our class "UserFlyweight" occupy 200 space rather 10000 space which User class will do
    """
    players = []
    for p_name in names:
        for p_family in families:
            players.append(UserFlyweight(f"{p_name} {p_family}"))

    print(players)
