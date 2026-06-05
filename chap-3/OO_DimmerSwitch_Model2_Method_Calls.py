# Regulador de Intensidade de Luz
class DimmerSwitch:
    def __init__(self, name):
        self.switchIsOn = False
        self.brightness = 0
        self.name = name

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print("Label: ", self.name)
        print("Switch is on ?", self.switchIsOn)
        print("Brightness is:", self.brightness)
        print()


oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer2 = DimmerSwitch('Dimmer2')

oDimmer1.raiseLevel()

oDimmer2.raiseLevel()
