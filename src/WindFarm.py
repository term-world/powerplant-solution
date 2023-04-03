from resources import Wind

class WindTurbine(Wind):

    def __init__(self, blade_size: int = 0):
        self.blade_size = 115
        super().__init__()