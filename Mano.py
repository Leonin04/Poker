from Baraja import Baraja
import random

class Mano:
    def __init__(self):
        self.cartas = []
        self.puntuación = 0

    def _inicializar_(self, baraja):
        for i in range(3):
            self.cartas.append(baraja.sacarCarta())

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)