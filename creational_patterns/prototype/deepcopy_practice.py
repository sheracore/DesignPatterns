import copy


class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def __str__(self):
        return f"{self.street} {self.city} {self.state}"


class Person:
    def __init__(self, first_name, last_name, address: Address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name} at {self.address}"

John = Person("John", "Smith", Address('Saffa', 'Tehran', 'Tehran'))
Jain = John
Jain.first_name = "Jain"
# both jain and john refer to one object, so their first_name is Jain because python is reference based
print(Jain)
print(John)

# To solve this problem use deepcopy
john = Person("John", "Smith", Address('Saffa', 'Tehran', 'Tehran'))
jain = copy.deepcopy(john)
jain.first_name = 'Jain'
jain.address.street = 'Jar'
print(john)
print(jain)
