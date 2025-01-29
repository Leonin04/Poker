from Baraja import Baraja
import random
from Funciones import orden
from Funciones import CheckMano

class Mano:
    def __init__(self):
        self.cartas = []
        self.puntuación = 0
        self.mano = []
        self.fichas = FICHAS

    def setPuntuacion(self, puntuacion):
        self.puntuación = puntuacion

    def getPuntuacion(self):
        return self.puntuación
    
    def getMano(self):
        return self.mano
    
    def getCartas(self):
        return self.cartas
    
    def comprobarMano(self, mesa):
        self.mano = CheckMano(mesa, self)
        

    def inicializar(self, baraja, n=2):
        for i in range(n):
            self.cartas.append(baraja.sacarCarta())
            self.puntuación += self.cartas[i].valor

    def pedirCarta(self, baraja):
        self.cartas.append(baraja.sacarCarta())
        self.puntuación += self.cartas[-1].valor

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)