from resources import Oil

class OilGenerator:

    def __init__(self):
        self.oil = Oil()
        self.energy = 0

    def use(self):
        for barrel in self.oil:
            self.energy += barrel.energy