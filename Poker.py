from Baraja import Baraja  
from Cartas import Carta
from Mano import Mano

baraja = Baraja()
miMano = Mano()
miMano._inicializar_(baraja)

print(miMano)