from client_code import client_code
from concreteClass1 import ConcreteClass1
from concreteClass2 import ConcreteClass2

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
