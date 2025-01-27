from Baraja import Baraja
import random

class Mano:
    def __init__(self):
        self.cartas = []
        self.puntuación = 0

    def getPuntuacion(self):
        return self.puntuación

    def inicializar(self, baraja, n=3):
        for i in range(n):
            self.cartas.append(baraja.sacarCarta())
            self.puntuación += self.cartas[i].valor

    def pedirCarta(self, baraja):
        self.cartas.append(baraja.sacarCarta())
        self.puntuación += self.cartas[-1].valor

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)