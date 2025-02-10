from context import Context
from concreteStrategyA import ConcreteStrategyA
from concreteStrategyB import ConcreteStrategyB


if __name__ == '__main__':
    # context = Context(ConcreteStrategyB)
    context = Context(ConcreteStrategyA)

    # context_b.do_some_business_logic()
    # context_a.do_some_business_logic()
    strategy = context.strategy()
    result = strategy.do_algorithm(['a', 't', 'b', 'x'])
    print(list(result))
