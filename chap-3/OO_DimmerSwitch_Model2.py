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


oDimmer1 = DimmerSwitch("Dimmer1")
print(type(oDimmer1))
print(oDimmer1)
print('oDimmer1 variables:', vars(oDimmer1))
print()

oDimmer2 = DimmerSwitch("Dimmer2")
print(type(oDimmer2))
print(oDimmer2)
print()

oDimmer3 = DimmerSwitch("Dimmer3")
print(type(oDimmer3))
print(oDimmer3)
print()
