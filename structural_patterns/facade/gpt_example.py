# -------------------------------- None facade -------------------------
class Light:
    def turn_on(self):
        print("Lights are ON")

    def turn_off(self):
        print("Lights are OFF")

class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

class AirConditioner:
    def turn_on(self):
        print("Air Conditioner is ON")

    def turn_off(self):
        print("Air Conditioner is OFF")

# Client code (complex interaction)
light = Light()
tv = TV()
ac = AirConditioner()

light.turn_on()
tv.turn_on()
ac.turn_on()

# -------------------------------- facade -------------------------
"""
Where to Use Facade Pattern?
APIs & Libraries: Wrapping complex APIs (e.g., interacting with third-party services like AWS, OpenAI, etc.).
Subsystems with Multiple Components: Managing large applications (e.g., multimedia players, game engines).
Database & ORM Wrappers: Simplifying database queries using a higher-level interface.
"""

class HomeAutomationFacade:
    def __init__(self):
        self.light = Light()
        self.tv = TV()
        self.ac = AirConditioner()

    def turn_everything_on(self):
        self.light.turn_on()
        self.tv.turn_on()
        self.ac.turn_on()
        print("All devices are ON")

    def turn_everything_off(self):
        self.light.turn_off()
        self.tv.turn_off()
        self.ac.turn_off()
        print("All devices are OFF")

# Client interacts with a single facade
home = HomeAutomationFacade()
home.turn_everything_on()
home.turn_everything_off()

