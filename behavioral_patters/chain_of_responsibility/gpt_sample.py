from abc import ABC, abstractmethod

# Abstract Handler
class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler  # Next handler in the chain

    @abstractmethod
    def handle_request(self, request):
        pass

# Concrete Handlers
class FrontDeskHandler(Handler):
    def handle_request(self, request):
        if request == "basic inquiry":
            print("Front Desk: Handling the basic inquiry.")
        elif self.next_handler:
            print("Front Desk: Forwarding request.")
            self.next_handler.handle_request(request)

class ManagerHandler(Handler):
    def handle_request(self, request):
        if request == "complex issue":
            print("Manager: Handling the complex issue.")
        elif self.next_handler:
            print("Manager: Forwarding request.")
            self.next_handler.handle_request(request)

class CEOHandler(Handler):
    def handle_request(self, request):
        print("CEO: Handling the high-priority request.")

# Creating the chain: FrontDesk → Manager → CEO
handler_chain = FrontDeskHandler(ManagerHandler(CEOHandler()))

# Test requests
handler_chain.handle_request("basic inquiry")
handler_chain.handle_request("complex issue")
handler_chain.handle_request("urgent escalation")