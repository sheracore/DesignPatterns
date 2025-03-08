from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Bitcoin.")

# Context (Payment Processor)
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Dynamically change the payment strategy."""
        self._strategy = strategy

    def process_payment(self, amount):
        """Delegate payment processing to the selected strategy."""
        self._strategy.pay(amount)

# Example Usage
processor = PaymentProcessor(CreditCardPayment())  # Default strategy
processor.process_payment(100)  # Paid $100 using Credit Card.

# Change payment method dynamically
processor.set_strategy(PayPalPayment())
processor.process_payment(200)  # Paid $200 using PayPal.

processor.set_strategy(BitcoinPayment())
processor.process_payment(300)  # Paid $300 using Bitcoin.