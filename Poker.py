from Baraja import Baraja  
from Cartas import Carta
from Mano import Mano
from Funciones import ComprobarMano
import os

baraja = Baraja()
miMano = Mano()
Mesa = Mano()
miMano.inicializar(baraja)
Mesa.inicializar(baraja,2)

print("Tus cartas son:")
print(miMano)
print("Tu puntuación es:",miMano.getPuntuacion())
print("Cartas de la mesa:")
print(Mesa)
print("Tu mano es: ", ComprobarMano(Mesa,miMano))

respuesta = input("¿Quieres otra carta? (s/n): ")
while respuesta.lower() == 's' and len(Mesa.cartas) < 5:
    os.system('cls' if os.name == 'nt' else 'clear')
    Mesa.pedirCarta(baraja)
    print("Tus cartas son:")
    print(miMano)
    print("Las cartas de la mesa son:")
    print(Mesa)
    print("Tu mano es: ", ComprobarMano(Mesa,miMano))
    if len(Mesa.cartas) < 5:
        respuesta = input("¿Quieres otra carta? (s/n): ")