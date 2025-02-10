from concreteSubject import ConcreteSubject
from concreteObserverA import ConcreteObserverA
from concreteObserverB import ConcreteObserverB

if __name__ == '__main__':
    # The client code.
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
