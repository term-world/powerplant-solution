from resources import Solar

class SolarPanel(Solar):

    def __init__(self, wattage: int = 300):
        self.wattage = wattage
        super().__init__()