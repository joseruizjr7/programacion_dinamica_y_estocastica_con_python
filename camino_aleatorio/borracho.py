import random

class Borracho:
    # inicializa el borracho
    def __init__(self, name):
        self.name = name

class BorrachoTradicional(Borracho):
    # inicializa el borracho tradicional
    def __init__(self, name):
        super().__init__(name)

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class BienBorracho(Borracho):
    def __init__(self, name):
        super().__init__(name)

    def camina(self):
        return random.choice([(0,1), (0,1), (0,-20), (19,0), (1,4), (-20,0)])