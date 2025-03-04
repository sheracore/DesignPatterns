class Memento:
    def __init__(self, balance):
        self.bank_account = BankAccount(balance)  # TODO: Inefficient, because it's generating a lot of objects

    def __str__(self):
        return f'{self.bank_account.balance}'

class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        return Memento(self.balance)

    def __str__(self):
        return f'{self.balance}'


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(40)
    m2 = ba.deposit(80)
    m3 = ba.deposit(55)
    print(ba)
    print(m1)
    print(m2)
    print(m3)


# ---------------------------------- Course Code ----------------------------------------


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f'Balance = {self.balance}'


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    # restore to m1
    ba.restore(m1)
    print(ba)

    # restore to m2
    ba.restore(m2)
    print(ba)