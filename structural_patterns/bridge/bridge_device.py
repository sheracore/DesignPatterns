from abc import ABC, abstractmethod

# -------------------------- without bridge -----------------------
# Combined abstraction and implementation
class BasicRemoteTV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

    def volume_up(self):
        print("TV volume increased")

    def volume_down(self):
        print("TV volume decreased")


class AdvancedRemoteTV(BasicRemoteTV):
    def mute(self):
        print("TV is muted")


class BasicRemoteRadio:
    def turn_on(self):
        print("Radio is ON")

    def turn_off(self):
        print("Radio is OFF")

    def volume_up(self):
        print("Radio volume increased")

    def volume_down(self):
        print("Radio volume decreased")


class AdvancedRemoteRadio(BasicRemoteRadio):
    def mute(self):
        print("Radio is muted")


# Client Code
if __name__ == "__main__":
    # Using BasicRemote for TV
    basic_tv_remote = BasicRemoteTV()
    basic_tv_remote.turn_on()  # TV is ON
    basic_tv_remote.volume_up()  # TV volume increased

    # Using AdvancedRemote for Radio
    advanced_radio_remote = AdvancedRemoteRadio()
    advanced_radio_remote.turn_on()  # Radio is ON
    advanced_radio_remote.mute()  # Radio is muted


# ----------------------------------- with bridge  -----------------------------------------

# Implementation Interface (Device)
class Device(ABC):
    @abstractmethod
    def is_on(self) -> bool:
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_volume(self, volume: int):
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

# Concrete Implementors (TV and Radio)
class TV(Device):
    def __init__(self):
        self._on = False
        self._volume = 50

    def is_on(self) -> bool:
        return self._on

    def turn_on(self):
        self._on = True
        print("TV is now ON")

    def turn_off(self):
        self._on = False
        print("TV is now OFF")

    def set_volume(self, volume: int):
        self._volume = max(0, min(volume, 100))  # Clamp volume between 0 and 100
        print(f"TV volume set to {self._volume}")

    def get_volume(self) -> int:
        return self._volume

class Radio(Device):
    def __init__(self):
        self._on = False
        self._volume = 30

    def is_on(self) -> bool:
        return self._on

    def turn_on(self):
        self._on = True
        print("Radio is now ON")

    def turn_off(self):
        self._on = False
        print("Radio is now OFF")

    def set_volume(self, volume: int):
        self._volume = max(0, min(volume, 100))  # Clamp volume between 0 and 100
        print(f"Radio volume set to {self._volume}")

    def get_volume(self) -> int:
        return self._volume

# Abstraction (RemoteControl)
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_on():
            self.device.turn_off()
        else:
            self.device.turn_on()

    def volume_up(self):
        current_volume = self.device.get_volume()
        self.device.set_volume(current_volume + 10)

    def volume_down(self):
        current_volume = self.device.get_volume()
        self.device.set_volume(current_volume - 10)

# Refined Abstraction (AdvancedRemoteControl)
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)
        print("Device is muted")

# Client Code
if __name__ == "__main__":
    # Using the Bridge pattern
    tv = TV()
    radio = Radio()

    basic_remote = RemoteControl(tv)
    advanced_remote = AdvancedRemoteControl(radio)

    # Test TV with Basic Remote
    basic_remote.toggle_power()  # TV is now ON
    basic_remote.volume_up()     # TV volume set to 60
    basic_remote.toggle_power()  # TV is now OFF

    print()

    # Test Radio with Advanced Remote
    advanced_remote.toggle_power()  # Radio is now ON
    advanced_remote.volume_down()   # Radio volume set to 20
    advanced_remote.mute()          # Device is muted