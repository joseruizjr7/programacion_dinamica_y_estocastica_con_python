class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def camina(self, otra_coord):
        delta_x = self.x - otra_coord.x
        delta_y = self.x - otra_coord.y

        return (delta_x**2 + delta_y**2)**0.5